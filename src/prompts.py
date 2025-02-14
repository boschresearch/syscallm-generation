# Copyright (c) 2025 Robert Bosch GmbH
# SPDX-License-Identifier: AGPL-3.0

def get_user_prompt(syscall_name: str, man_page: str, mode: str) -> str:
    if mode == "success":
        return f"""
For the system call `{syscall_name}`, generate a JSON with test_values (a list of integer values to inject as successful return values).

These values should include:
- Typical return values expected for successful execution, as documented in the manual page (e.g., 0 for `close`, number of bytes read for `read`).
- Uncommon but valid return values that may indicate edge cases, boundary conditions, or rarely observed behaviors (e.g., small positive integers that are syntactically valid but less common, such as 5 for `close`).

The goal is to support robust and adversarial testing of the system call’s handling of success cases, including both standard behavior and plausible edge cases.

Ensure that:
- All values are valid unsigned 64-bit integers (i.e., between 0 and 18446744073709551615).
- All values are unique.

Use the following manual page as reference:

{man_page}
"""

    elif mode == "error_code":
        return f"""
For the system call `{syscall_name}`, generate a JSON with error_codes (a list of error codes to inject as failure return values).

These should include:
- Expected error codes documented in the manual page (e.g., `EIO`, `EBADF`).
- Unexpected or undocumented error codes not typically associated with this system call (e.g., `ECHILD` for `read`), which may arise due to kernel bugs, resource misuse, race conditions, or anomalous behavior.

The goal is to enable robust and adversarial testing of error-handling logic, including both normative and edge-case behaviors.

Ensure that:
- All error codes start with 'E' and follow standard errno naming.
- All error codes are unique.

Use the following manual page as reference:

{man_page}
"""

def get_message_list(syscall_name: str, man_page: str, mode: str) -> list[dict]:
    return [
        {"role": "system", "content": "You are a helpful assistant that generates test values for system call returns error injection based on man pages."},
        {"role": "user", "content": get_user_prompt(syscall_name, man_page, mode)}
    ]
        
