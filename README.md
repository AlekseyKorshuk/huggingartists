# HuggingArtists - Train a model to generate lyrics

## Create AI-Artist in just 5 minutes!

<img src="img/logo.jpg" width="420" align="center">

### [🚀 Run the demo](https://colab.research.google.com/github/AlekseyKorshuk/huggingartists/blob/master/huggingartists-demo.ipynb)

_Disclaimer: this project is not to be used to publish any false generated information or unpleasant words but to perform research on Natural Language Generation._

## How to use

To test the demo, click on below link and share your results!

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/AlekseyKorshuk/huggingartists/blob/master/huggingartists-demo.ipynb)

You can also use it locally by installing the dependencies with `pipenv` or `pip` and use [`huggingartists-demo.ipynb`](huggingartists-demo.ipynb)

## Results

There are some interesting lyrics. Contact me to add your results:

#### Eminem:
~~~
I am a bit of a nutter
Like a fucking crazy nut
But I just wanted to break and get a little more serious, so be patient
I dont think I need no medical attention
But I do know that these niggas gonna be in my prayers
And they say Im a nutter
Like a fucking crazy nut
But I love you
I am a nutter
Like a fuckin nutter
But I feel like the greatest that I can be
With your body and your spirits
But I dont know how I will act
When I finally get out
And I get pissed off
Ill be right back at ya with the first one on the floor
But I aint ever gonna get the respect youve been getting
And Im a nutter
~~~

#### Drake:
~~~
I am what they say I am
In a barroom brawlin
Youre never gonna get me up like Jada Pinkett
So this what they call me
Livin a fight while Im sippin on Hennessy
My name is Kala Brown, I need a new name
Cause I dont live a bitch
Dont play the same shit I did before
I dont lie and nobody wanna know
I got a little group on my shoulders to save
I want to be a man but I gotta do a lot of things to get me there
So get over yourself, get over yourselves
Its like you and I dont care how we do it
But youll get there when you get there
Cause it feels good to be me
Cause I know
~~~

## Check existing:
* [Models](https://huggingface.co/models?filter=huggingartists)
* [Datasets](https://huggingface.co/datasets?filter=huggingartists)


## Features:
* Generate lyrics by a specific artist
* Automatically upload models and datasets to [HuggingFace Profile](https://huggingface.co/huggingartists) after each each run
* Parse dataset once and use it next time without spending time
* Each next run by any person will resume training from checkpoint
* Training and results are automatically logged into [W&B](https://docs.wandb.com) through the [HuggingFace integration](https://docs.wandb.com/huggingface)


## About

*Built by Aleksey Korshuk*

[![Follow](https://img.shields.io/github/followers/AlekseyKorshuk?style=social)](https://github.com/AlekseyKorshuk)

🚀 If you want to contribute to this project OR create something cool, contact me: [link](https://github.com/AlekseyKorshuk)

Star this repository:

[![GitHub stars](https://img.shields.io/github/stars/AlekseyKorshuk/huggingartists?style=social)](https://github.com/AlekseyKorshuk/huggingartists)

**Disclaimer: this project is not to be used to publish any false generated information or unpleasant words but to perform research on Natural Language Generation.**

## Resources
* Inspired by [HuggingTweets](https://github.com/borisdayma/huggingtweets)
* [Explore the W&B report](https://wandb.ai/huggingartists/huggingartists/reportlist) to understand how the model works
* [HuggingFace and W&B integration documentation](https://docs.wandb.com/library/integrations/huggingface)

## Got questions about W&B?
If you have any questions about using W&B to track your model performance and predictions, please reach out to the [slack community](https://wb-forum.slack.com/signup#/).
