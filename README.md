# notion-py-translator
CLI tool to translate Notion pages into a different language (use google translate)
Notion PyTranslator is a CLI tool that enables Notion users to use translate Notion pages into a different language by using Google Translate API.

How It Works
1. Create Notion Api Token
    https://www.notion.so/my-integrations
2. Duplicate the page which will translate
3. Add connect to duplicated page
    https://www.notion.so/help/add-and-manage-connections-with-the-api#add-connections-to-pages
4. check the language code
    https://cloud.google.com/translate/docs/languages

Run the following command to translate duplicated page automatically

`pynotion_translate.py <notion api token> <language code> <notion url>`


## License

The MIT License
