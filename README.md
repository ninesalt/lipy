<div align = "center">

<img src = "https://i.imgur.com/dPNgXVy.png" with="300" height="300"/>

</div>

## What is  Lipy ?

Lipy is a machine learning model that predicts which image from a set of images has the highest probability of getting liked the most on Instagram. This is still very much a work in progress. 

## How does it work?

Lipy uses [Keras](https://keras.io/) (with TensorFlow as its backend) to build a convolutional neural network. The network is then trained on a series of images that were previously scraped (see `./scraper`) and their corresponding number of likes which are normalized to remove the correlation between number of followers and the number of likes. 

The goal is that upon completion, the model will be given `N` images and will choose the "best" one. The best case scenario would be if model didn't have to predict the number of likes the image will get and rather it would predict from any two images, which one will score the highest. This will likely lead to better accuracy/score.

## Roadmap
- Complete initial model and compare with other models with a similar architecture. 
- Write dockerfile for the scraping component to allow deployment on cloud machines (scraping usually takes a while if many accounts are scraped).
- Create API endpoints for public use.
- Create frontend interface.
- Deploy API and frontend

## License 

MIT License