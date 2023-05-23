# notion-py-translator
CLI tool to translate Notion pages into a different language (use google translate)

Notion PyTranslator is a CLI tool that enables Notion users to use translate Notion pages into a different language by using Google Translate API.

How It Works
1. Create Notion Api Token
    https://www.notion.so/my-integrations
2. Duplicate the page which will translate
3. Add connect to duplicated page
    https://www.notion.so/help/add-and-manage-connections-with-the-api#add-connections-to-pages

Run the following command to translate duplicated page automatically

Create a Notion internal integration and save its token as NOTION_API_TOKEN env variable
Create a DeepL API account and save its token as DEEPL_API_TOKEN env variable
Share the target Notion page with your Notion integration
Run the following command to generate a translated page automatically
python pynotion_translate.py <url> <token> <language>
