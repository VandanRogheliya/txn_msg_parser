from __future__ import annotations
import json

from txn_msg_parser.constants import OUTPUT_FORMAT
from txn_msg_parser.training_data.sms_training import sms_training_data


class PromptGenFactory:
    def get_sms_txn_parsing_prompt(
        self,
        input_dict: dict,
        categories: list[str] | None,
        accounts: list[str] | None,
        sms_training_data_arg: list[dict],
    ) -> str:
        examples = sms_training_data_arg if sms_training_data_arg else sms_training_data
        skipped_keys = set()
        if not accounts:
            skipped_keys.add("account")
        if not categories:
            skipped_keys.add("category")
        if skipped_keys:
            examples = [
                {
                    **ex,
                    "output": {
                        k: v for k, v in ex["output"].items() if k not in skipped_keys
                    },
                }
                for ex in examples
            ]
        sms_training_data_json = json.dumps(examples)
        input_json = json.dumps(input_dict)
        output_format = {
            k: v for k, v in OUTPUT_FORMAT.items() if k not in skipped_keys
        }
        output_format_json = json.dumps(output_format)
        context_items = [
            f'Account -> From "sender" key. Valid values: {accounts}'
            if accounts
            else None,
            'Amount -> From "text" key. Keep it as a number with decimals. Examples: 100.5 -> 100.5, 145 -> 145, 42,523.47 -> 42523.47',
            'Transaction type -> From "text" key. Valid values: "credit", "debit"',
            'Payee -> From "text" key, String about who is receiving payment. Null for credit type',
            'Payer -> From "text" key, String about who sent the payment. Null for debit type',
            f'Category -> From "text" key, One word category for txn. Valid categories: {categories}'
            if categories
            else None,
        ]
        context = "\n".join(
            f"{i}. {item}"
            for i, item in enumerate((c for c in context_items if c), start=1)
        )
        prompt = f"""
Refer to these examples and learn how to convert a transaction SMS object to transaction JSON object.

<context>
{context}

</context>

<examples>
{sms_training_data_json}
</examples>

SMS input JSON to convert:
<input>
{input_json}
</input>

Reply only in JSON.
Output JSON format:
<output-format>
{output_format_json}
</output-format>

"""
        return prompt
