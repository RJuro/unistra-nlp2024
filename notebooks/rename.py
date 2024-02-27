import os

# Mapping of original filenames to new filenames
filename_mapping = {
    "UNISTRA-01-NLP101-Classification.ipynb": "01-UNISTRA-NLP101-Classification.ipynb",
    "UNISTRA-02\\FewShot-classifier-argilla-setfit.ipynb.ipynb": "02-UNISTRA-FewShot-Classifier-Argilla-SetFit.ipynb",
    "UNISTRA-03\\ZeroShot-classifier-argilla-setfit-LLM.ipynb.ipynb": "03-UNISTRA-ZeroShot-Classifier-Argilla-SetFit-LLM.ipynb",
    "UNISTRA-04\\TMOpenAITogether.ipynb.ipynb": "04-UNISTRA-TM-OpenAI-Together.ipynb",
    "UNISTRA-05\\SimpleQA-Retriever.ipynb.ipynb": "05-UNISTRA-SimpleQA-Retriever.ipynb",
    "UNISTRA-06\\SelfQuery-Retriever.ipynb.ipynb": "06-UNISTRA-SelfQuery-Retriever.ipynb",
    "UNISTRA-07\\LLMLabelSynthesis.ipynb.ipynb": "07-UNISTRA-LLM-Label-Synthesis.ipynb",
    "UNISTRA-08\\Mistral7bFinetunePatent.ipynb.ipynb": "08-UNISTRA-Mistral7b-Finetune-Patent.ipynb"
}

# Function to rename files based on the mapping
def rename_files(mapping):
    for original, new in mapping.items():
        # Correcting the original path if it contains backslashes
        original_corrected = original.replace("\\", "/")  # Use this line if running on Unix/Linux/Mac
        # original_corrected = original  # Use this line if running on Windows and the path is correct
        
        # Check if the original file exists
        if os.path.exists(original_corrected):
            # Rename the file
            os.rename(original_corrected, new)
            print(f'Renamed "{original}" to "{new}"')
        else:
            print(f'File "{original}" not found.')

# Call the function with the filename mapping
rename_files(filename_mapping)