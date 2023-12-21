import os

# Define the directory where the transcripts are stored
transcripts_dir = "../transcripts/"

# Define the output file
output_file = "combined_transcripts.txt"

# Open the output file in write mode
with open(output_file, "w") as outfile:
    # Loop over all files in the transcripts directory
    for filename in os.listdir(transcripts_dir):
        # Check if the file is a .txt file
        if filename.endswith(".txt"):
            # Open the transcript file in read mode
            with open(transcripts_dir + filename, "r") as readfile:
                # Write the contents of the transcript file to the output file
                outfile.write(readfile.read())
                # Add a newline character to separate transcripts
                outfile.write("\n")
