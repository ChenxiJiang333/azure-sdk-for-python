Follow the steps with order:
    1. step into folder `packages/http-client-python/generator/test`
    2. run `npm install`
    3. run `npm run build`
    4. run `npm run regenerate`
    5. search the TypeSpec code of scenario `AlternateApiVersion.Service.Header` from https://github.com/Azure/typespec-azure/blob/main/packages/azure-http-specs/specs
    6. look for the test files generated from the TypeSpec code from local folder `azure/generated`
    7. find in file `azure/requirements.txt` to check if there is a requirement for the generated package, if no, add it in
    8. find in folder `azure/mock_api_tests` to check if there is a mock api test file sharing the same namespace, if no, create one
    9. translate testcases from the generated test files and add them into the mock API test file if they do not exist in it, no need to add annotations
    10. do the same thing for *_aysnc.py file under folder `asynctests` and respect the async pattern
    11. run `npm run format`
    12. run `npm run change:add`, select `@typespec/http-client-python` then `internal` then input message "Add testcases for several spector scenarios"