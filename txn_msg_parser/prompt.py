from __future__ import annotations
import json
from txn_msg_parser.constants import OUTPUT_FORMAT
from txn_msg_parser.training_data.sms_training import sms_training_data


class PromptGenFactory:
    def get_sms_txn_parsing_prompt(
        self, input_dict: dict, categories: list[str], accounts: list[str], sms_training_data_arg: list[dict]
    ) -> str:
        examples = sms_training_data_arg if sms_training_data_arg else sms_training_data
        if not categories:
            examples = [
                {**ex, "output": {k: v for k, v in ex["output"].items() if k != "category"}}
                for ex in examples
            ]
        sms_training_data_json = json.dumps(examples)
        input_json = json.dumps(input_dict)
        output_format = OUTPUT_FORMAT.copy()
        if not categories:
            output_format.pop("category", None)
        output_format_json = json.dumps(output_format)
        prompt = f"""
Refer to these examples and learn how to convert a transaction SMS object to transaction JSON object.

<context>
1. Account -> From "sender" key. Valid values: {accounts}
2. Amount -> From "text" key. Keep it as a number with decimals. Examples: 100.5 -> 100.5, 145 -> 145, 42,523.47 -> 42523.47
3. Transaction type -> From "text" key. Value values: "credit", "debit"
4. Payee -> From "text" key, String about who is receiving payment. Null for credit type
5. Payer -> From "text" key, String about who sent the payment. Null for debit type
{f'6. Category -> From "text" key, One word category for txn. Valid categories: {categories}' if categories else ""}

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
