import os
import tiktoken

# Define the directory where the transcripts are stored
transcripts_dir = "../transcripts/"

# Define the output file
output_file = "combined_transcripts_{}.txt"

# Initialize the encoder
encoding = tiktoken.encoding_for_model("gpt-4-1106-preview")

# Initialize the token count and file count
token_count = 0
file_count = 0

# Open the first output file in write mode
outfile = open(output_file.format(file_count), "w")

# Loop over all files in the transcripts directory
for filename in os.listdir(transcripts_dir):
    # Check if the file is a .txt file
    if filename.endswith(".txt"):
        # Open the transcript file in read mode
        with open(transcripts_dir + filename, "r") as readfile:
            # Read the contents of the transcript file
            content = readfile.read()
            
            # Count the tokens in the content
            num_tokens = len(encoding.encode(content))
            
            # If adding this content would exceed the limit
            if token_count + num_tokens > 1000000:
                # Close the current output file
                outfile.close()
                
                # Increment the file count
                file_count += 1
                
                # Open a new output file
                outfile = open(output_file.format(file_count), "w")
                
                # Reset the token count
                token_count = 0
            
            # Write the contents of the transcript file to the output file
            outfile.write(content)
            
            # Add a newline character to separate transcripts
            outfile.write("\n")
            
            # Update the token count
            token_count += num_tokens

# Close the last output file
outfile.close()