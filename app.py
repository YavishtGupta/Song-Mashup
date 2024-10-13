from flask import Flask, render_template, request, send_file
import time
import os

app = Flask(__name__)

# Function to run the pipeline
def run_pipeline():
    scripts = [
        "download_yt_videos.py",
        "video_to_audio.py",
        "trim_audio.py",
        "merge_audio.py"
    ]
    
    output = ""
    total_start_time = time.time()

    for script in scripts:
        output += f"Running {script}...\n"
        start_time = time.time()
        result = os.system(f'python {script}')
        elapsed_time = time.time() - start_time
        if result != 0:
            output += f"Error: {script} failed to run.\n"
            break
        output += f"{script} completed successfully in {elapsed_time:.2f} seconds.\n"
    
    total_elapsed_time = time.time() - total_start_time
    output += f"\nAll scripts completed successfully! Total time taken: {total_elapsed_time:.2f} seconds."
    
    # Path to the final output audio file
    output_audio_file_path = 'output.mp3'  
    return output_audio_file_path, output

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run', methods=['POST'])
def run():
    # When the form is submitted, run the pipeline
    output_audio_file_path, output = run_pipeline()
    return render_template('index.html', output=output, output_file=output_audio_file_path)

@app.route('/download')
def download_file():
    # Send the audio file for download
    return send_file('output.mp3', as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
