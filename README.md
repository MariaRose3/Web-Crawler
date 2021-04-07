# Web-Crawler
Project for Winter of Code 3.0

IIT (ISM) Dhanbad

The crawler takes only four arguments, '-u' is the URL to be crawled, '-d' is the depth of the crawler, '-o' is the name of the directory in which the results will be stored and '-b' is the number of threads.
It only crawls the links in the given domain. When encountered with links from other domains, they are collected and stored in another file in the same directory.

The basic idea is that all the links extracted in the first crawl are stored in a file called queue.txt. Then the links needed for each thread is extracted from this file. One these links are crawled the crawled links are stored in another file called crawled.txt and then removed from queue.txt. The result obtained in the next crawl is then added to queue.txt, provided it is not in crawled.txt. This ensures that the same links are not crawled again. All the above mentioned files are in a directory whose name you have to specify on the command line.

Aknowledgement: The idea and the script is inspired by various online sourses.

Note: The project is not complete and the CLI functionality is not yet implemented in main.py. The script might also need to be debugged. I pushed my code as I was running out of time.

Thank you
