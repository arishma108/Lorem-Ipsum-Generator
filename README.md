# Lorem-Ipsum-Generator
This function generates random "Lorem Ipsum" text, a placeholder text commonly used in the design industry to demonstrate the visual effects of different typefaces and layouts.

## Function Name: "Lorem Ipsum Generator"
### Programming Language: Python

#### Description:
This function generates random "Lorem Ipsum" text, a placeholder text commonly used in the design industry to demonstrate the visual effects of different typefaces and layouts.

#### Functionality:

The function takes a single integer input, "num_paragraphs", representing the number of paragraphs of Lorem Ipsum text to generate.
The function generates the specified number of paragraphs of Lorem Ipsum text using Python's built-in "random" module and a pre-defined list of Lorem Ipsum words and phrases.
The function returns the generated Lorem Ipsum text as a string.

##### Example Usage:
If the user specifies "num_paragraphs=3", the function could generate output similar to the following:

"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam viverra eros magna, sit amet dignissim quam bibendum a. In hac habitasse platea dictumst. Donec eleifend, velit eget bibendum iaculis, justo nulla suscipit libero, ac interdum est nunc vitae odio.

Praesent vel ornare turpis. Maecenas sed elit elit. Curabitur imperdiet fringilla orci, a rutrum libero bibendum vel. Fusce iaculis, ipsum eu ultricies venenatis, tortor lectus bibendum ante, vel suscipit nibh mi eget augue.

Suspendisse potenti. Etiam aliquet, quam eu consequat fringilla, diam diam malesuada diam, ac interdum quam ipsum non odio. Praesent maximus eget nulla vel bibendum. Nullam eget ultricies erat, vel auctor quam. Aliquam et dolor eget augue vestibulum euismod. "

This function could be useful for developers who need to generate placeholder text for their design projects or test cases. It also demonstrates how easy it is to create a simple function with OpenFaaS that can be used to solve specific problems or automate certain tasks.

#### Prerequisites:

You must have OpenFaaS installed and configured on your local machine or server. You can follow the official installation guide on the OpenFaaS website (https://docs.openfaas.com/deployment/) to set up your environment.
You must have the "faas-cli" command-line tool installed. You can download and install it from the official OpenFaaS GitHub repository (https://github.com/openfaas/faas-cli).

#### Steps to use the "Lorem Ipsum Generator" function:

1. Clone the "Lorem Ipsum Generator" function repository from GitHub (https://github.com/example/lorem-ipsum-generator) to your local machine or server.
2. Navigate to the cloned repository directory in your terminal or command prompt.
3. Use the "faas-cli" tool to deploy the function to your OpenFaaS environment:

```
faas-cli deploy -f lorem-ipsum-generator.yml
```
4. Once the function is deployed, you can invoke it using the "faas-cli" tool:

```
faas-cli invoke lorem-ipsum-generator --query num_paragraphs=3
```

here we are invoking the function with the "num_paragraphs" input set to 3. You can adjust this value as needed.
The function will generate the specified number of paragraphs of Lorem Ipsum text and return it as a string output in your terminal or command prompt.
You can use this function whenever you need to generate random placeholder text for your projects or testing. You can also modify the function code to customize the list of Lorem Ipsum words and phrases used to generate the text.

'lorem-ipsum-generator.yml': This is the function definition file for OpenFaaS. It defines the Docker image to use, the function name, and other configuration options. 
'requirements.txt': This file lists the Python dependencies required by the function. In this case, we only have one dependency, which is flask. 
'handler.py': This is the Python script that contains the function code. It defines the handle() function that generates the Lorem Ipsum text. Here's an example content of the file:

These files are all included in the "Lorem Ipsum Generator" function repository if you cloned it from my GitHub.

Created by: #### Darshani Persadh <a href="https://github.com/arishma108"></a>
