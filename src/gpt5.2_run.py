# Copyright (c) 2025 Robert Bosch GmbH
# SPDX-License-Identifier: AGPL-3.0

import os
import argparse
import json
from openai import OpenAI
import output_json_schema
import prompts

# parameters
model_name = "gpt-5.2"
deployment_name = "gpt-5.2"
endpoint = os.environ.get("OPENAI_ENDPOINT")
api_key = os.environ.get("OPENAI_API_KEY")

def get_client():
    return OpenAI(
        base_url=f"{endpoint}",
        api_key=api_key
    )

def read_man_page(man_file_path):
    with open(man_file_path, 'r') as file:
        return file.read()

def write_to_file(file_path, data):
    with open(file_path, 'w') as file:
        file.write(data)

def main(man_dir_path, output_dir_path, mode):
    client = get_client()

    os.makedirs(output_dir_path, exist_ok=True)

    for man_file_name in os.listdir(man_dir_path):
        man_file_path = os.path.join(man_dir_path, man_file_name)
        print(f"{man_file_path}: ", end='')
        
        # read man page
        man_page = read_man_page(man_file_path)

        # extract syscall name
        syscall_name = man_file_name.split('.txt')[0]

        # output file path
        output_man_file_path = os.path.join(output_dir_path, f'{syscall_name}.json')

        # user role prompts
        message_list = prompts.get_message_list(syscall_name, man_page, mode)

        if mode == "success":
            schema = output_json_schema.SyscallSuccess
        elif mode == "error_code":
            schema = output_json_schema.SyscallErrorCode
        
        try:
            completion = client.beta.chat.completions.parse(
                model=deployment_name,
                messages=message_list,
                max_completion_tokens=4096,
                response_format=schema
            )
        except Exception as e:
            print(f"ERROR - {repr(e)}")
            write_to_file(output_man_file_path, repr(e))
            continue

        # count number of tokens of the response
        output_token_size = completion.usage.completion_tokens
        total_token_size = completion.usage.total_tokens
        print(f"{output_token_size} / {total_token_size}")
            
        try:
            output = completion.choices[0].message

            if output.refusal:
                write_to_file(output_man_file_path, output.refusal)
            else:
                write_to_file(output_man_file_path, output.parsed.model_dump_json(indent=2))

        except (IndexError, AttributeError, TypeError, json.JSONDecodeError) as e:
            write_to_file(output_man_file_path, repr(e))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process man pages and generate JSON output.')
    parser.add_argument('--output_dir_path', type=str, help='The output directory path for JSON files.')
    parser.add_argument('--man_dir_path', type=str, default='man', help='The directory path for man files.')
    parser.add_argument("--mode", type=str, required=True, help="Error injection mode (e.g., 'error_code', 'success')")
    args = parser.parse_args()

    main(args.man_dir_path, args.output_dir_path, args.mode)
