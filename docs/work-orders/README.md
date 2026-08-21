# Work Orders

Store one strict JSON file per write task. Use the generated scaffold command, keep scopes
small, and never reuse a receipt across candidates or customers. Historical receipts are
audit evidence and must not contain credentials, private-key material or raw customer data.
Use `small` unless scope evidence justifies a larger effort class. When a round limit is reached,
stop and re-plan instead of starting another implementation or review loop.
