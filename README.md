# nano-gemini-cli

A dynamic Python CLI tool for managing prompts and generating images via Google’s Gemini 2.5 Flash Image API.

## Features

- Add and manage text prompts interactively
- List saved prompts for easy reuse
- Send prompts to Gemini 2.5 Flash Image API
- Display and handle API responses with robust error feedback
- Simple, extensible CLI workflow

## Requirements

- Python 3.7+
- [requests](https://pypi.org/project/requests/) library  
  Install via:  

 ``` pip install requests ```

- Gemini API key  
- Obtain from [Google AI Studio](https://aistudio.google.com/)

## Installation

1. Clone the repository:

``` git clone https://github.com/yourusername/nano-gemini-cli.git ```
``` cd nano-gemini-cli ```

2. Install dependencies:-

```pip install requests```


## Usage

1. Set your Gemini API key in the code (replace `YOUR_GEMINI_API_KEY`).

2. Run the CLI app:

```python nano_gemini_cli.py```


3. Use the interactive menu:
- **Add Prompt:** Enter new prompts to save and use
- **List Prompts:** View all saved prompts
- **Generate Image:** Select a prompt and send it to Gemini API
- **Exit:** Quit the application

## Example

=== Nano Banana Gemini App ===

Add Prompt

List Prompts

Generate Image

Exit

Choose: 1
Enter prompt: A panda eating banana in a city park
Prompt added.
Choose: 3
Select prompt number: 1
Response from Gemini API:
{ ... }


## Configuration

- Find your Gemini API key at [Google AI Studio](https://aistudio.google.com/).
- Replace `"YOUR_GEMINI_API_KEY"` in the script with your actual key.

## Project Structure

```nano_gemini_cli.py # Main Python CLI script```
```README.md # This file```

## License

MIT

---

**nano-gemini-cli** streamlines prompt management and image creation for creators, educators, and developers using Gemini’s API.

Questions or contributions? Open an issue or pull request!
