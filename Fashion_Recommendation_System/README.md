# FASHION RECOMMENDATION SYSTEM

A Fashion Recommendation System using Image Features leverages computer vision and machine learning techniques to analyze fashion items’ visual aspects (like colour, texture, and style) and recommend similar or complementary products to users.

## Process Flow

1. Assemble a diverse dataset of fashion items. This dataset should include a wide variety of items with different colours, patterns, styles, and categories.
   
2. Ensure all images are in a consistent format (e.g., JPEG, PNG) and resolution.

3. Implement a preprocessing function to prepare images for feature extraction.

4. Choose a pre-trained CNN model such as VGG16, ResNet, or InceptionV3. These models, pre-trained on large datasets like ImageNet, are capable of extracting powerful feature representations from images.

5. Pass each image through the CNN model to extract features.

6. Define a metric for measuring the similarity between feature vectors. 

7. Rank the dataset images based on their similarity to the input image and recommend the top N items that are most similar.

8. Implement a final function that encapsulates the entire process from pre-processing an input image, extracting features, computing similarities, and outputting recommendations.

### Issues Faced during Building this Model

Default import to tensorflow gave TypeError as below

import tensorflow as tf  

<b>Error:</b>

TypeError: Descriptors cannot not be created directly.
If this call came from a _pb2.py file, your generated code is out of date and must be regenerated with protoc >= 3.19.0.
If you cannot immediately regenerate your protos, some other possible workarounds are:
 1. Downgrade the protobuf package to 3.20.x or lower.
 2. Set PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION=python (but this will use pure-Python parsing and will be much slower).

<b>Suggestions:</b>
https://stackoverflow.com/questions/72441758/typeerror-descriptors-cannot-not-be-created-directly

Multiple solutions tried:

1.  Downgraded protobuf to 3.20.x , then 3.20.3 and then 3.20.1 
2.  installed tensorflow 2.9.1
3.  set environment variable in cmd prompt

C:\Users\deept>setx PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION python

SUCCESS: Specified value was saved.

<b>All the codes started working</b>

Also tried below step it worked

Executed import tensorflow statement in colab - worked



