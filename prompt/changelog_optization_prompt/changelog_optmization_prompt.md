Optimize this changelog for the latest version by following rules below, only do necessary updates that the log completely meets the condition of the rules and respect the format:

1. "Added model ...Operations" -> "Added operation group ...Operations"
2. "`A` removed default value None from its parameter `B`" -> "Parameter `B` of `A` is now required"
3. "`A` parameter `B` changed default value from ... to none" -> "Parameter `B` of `A` is now optional"
4. Remove "Client `...` added method `send_request`"
5. Remove "Method `...` has a new overload `...`"
6. Remove "Model `...` deleted or renamed its instance variable `additional_properties`"
7. If "*`A` inserted a `positional_or_keyword` parameter `C`*" & "*`A` deleted or renamed its parameter `B` of kind `positional_or_keyword`*" exist together, merged them in to *`A` renamed its instance variable `B` to `C`*