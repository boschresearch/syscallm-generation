# LLM-Based System Call Error Injection Test Generation

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Shell Script](https://img.shields.io/badge/shell_script-%23121011.svg?style=for-the-badge&logo=gnu-bash&logoColor=white)

This repository provides scripts and prompts for generating system call error injection tests using large language models (LLMs) based on the system call manual pages. The goal is to automate the creation of test cases that simulate various system call failures, improving the robustness and reliability of software systems.

## Features

- **Manual Page Extraction:** Automatically extracts relevant system call manual pages to inform test generation.
- **Automated Test Generation:** Leverages LLMs to generate test cases for system call error handling.
- **Customizable Scenarios:** Supports configuration of target system calls and error conditions.

## Hardware Requirements

For optimal performance, especially when generating large numbers of test cases, a system with a modern GPU is recommended. The following hardware is suggested:

- **GPU:** NVIDIA GPU with at least 8GB VRAM
- **CUDA Support:** Ensure CUDA drivers are installed for GPU acceleration
- **RAM:** Minimum 16GB system memory
- **Storage:** At least 10GB free disk space for models and generated tests

CPU-only operation is possible but will be significantly slower.

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/boschresearch/syscallm-generation.git
    cd syscallm-generation
    ```

2. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Getting Started

1. **Extract manual pages:**
   ```bash
   bash ./scripts/extract_syscall_man_pages.sh
   ```
   
2. **Set `OPENAI_ENDPOINT` and `OPENAI_API_KEY` as environment variable:** (for Open AI models)
   ```bash
    # if you are using bash
    echo 'export OPENAI_ENDPOINT="your_endpoint_here"' >> ~/.bashrc
    echo 'export OPENAI_API_KEY="your_key_here"' >> ~/.bashrc
    # if you are using zsh
    echo 'export OPENAI_ENDPOINT="your_endpoint_here"' >> ~/.zshrc
    echo 'export OPENAI_API_KEY="your_key_here"' >> ~/.zshrc
   ```

3. **Generate tests:**
    ```bash
    bash ./scripts/run.sh
    ```

## Supported LLMs

Tested LLMs are:
- GPT-5.2

## Open Source Software
This project relies on the usage of open-source Python libraries.

| Name          | License                    |
|---------------|----------------------------|
| openai        | MIT                        |
| pydantic      | MIT                        |

## Contact

For any questions or issues, please contact [Min Hee Jo](mailto:MinHee.Jo@de.bosch.com).

## License

SyscaLLM-Generation is open-sourced under the AGPL-3.0 license. See the LICENSE file for details.
