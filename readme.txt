For basic use, you need to specify in the config the folder where the search will be performed, the target object, whether to move or copy separately found images, as well as the search depth: 'easy' for quick search, 'medium' for medium, and 'hard' for deep search.

The search uses the compact and fast llava model running in ollama. To run it, you need to install ollama and the model itself, and on some Linux distributions also run:

curl -fsSSL https://ollama.com/install.sh | sh
ollama pull llava
#for some distributions, you will also need to enter and leave running before use
ollama run llava
