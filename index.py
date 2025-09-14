import requests

class NanoBananaGeminiApp:
    def __init__(self, api_key):
        self.prompts = []
        self.api_key = api_key
        # Correct API endpoint for Gemini 2.5 Flash Image (with no key yet)
        self.api_url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-image-preview:generateContent"

    def add_prompt(self, prompt):
        self.prompts.append(prompt)
        print("Prompt added.")

    def list_prompts(self):
        if not self.prompts:
            print("No prompts added yet.")
        else:
            for idx, prompt in enumerate(self.prompts, 1):
                print(f"{idx}. {prompt}")

    def generate_image(self, prompt):
        params = {"key": self.api_key}
        data = {
            "contents": [
                {
                    "parts": [
                        {"text": prompt}
                    ]
                }
            ]
        }
        try:
            response = requests.post(self.api_url, params=params, json=data)
            result = response.json()
            if response.status_code == 200:
                # The actual field with the generated image or result may vary.
                # Adjust as per the returned JSON structure.
                print("Response from Gemini API:")
                print(result)
                # You may extract and display image URL as needed.
            else:
                print("Failed to generate image.")
                print(result)
        except Exception as e:
            print("Error during request:", e)

    def run(self):
        print("=== Nano Banana Gemini App ===")
        while True:
            print("\n1. Add Prompt\n2. List Prompts\n3. Generate Image\n4. Exit")
            choice = input("Choose: ")
            if choice == '1':
                p = input("Enter prompt: ")
                self.add_prompt(p)
            elif choice == '2':
                self.list_prompts()
            elif choice == '3':
                if not self.prompts:
                    print("No prompts available. Add one first.")
                    continue
                self.list_prompts()
                idx = int(input("Select prompt number: "))
                prompt = self.prompts[idx-1]
                self.generate_image(prompt)
            elif choice == '4':
                print("Exiting. Goodbye!")
                break
            else:
                print("Invalid input")

if __name__ == "__main__":
    # Replace this with your actual API key from Google AI Studio!
    api_key = "AIzaSyATAjRBEzxFkNcQcfpCkkEM-o7kQks4TdE"
    app = NanoBananaGeminiApp(api_key)
    app.run()
