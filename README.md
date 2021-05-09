# Big-Data-Project
To run the program, open up main.py and change - The input folder for the images, and the Database connection information to store the info in a database.

To run the database, we used XAMPP and used the following schema:
- id: Co-key, id of the image from the open images dataset
- compression_type: Co-key, The algorithm the image was compressed with (“copy” for the baseline image)
- time_elapsed: Time taken to compress the image (time taken to copy for the uncompressed image)
- num_bytes: Size of the image
- img_data_path: The location of the compressed image
- file_type: The type of the file
