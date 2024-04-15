# shrek-frame

![GitHub License](https://img.shields.io/github/license/Kamix-08/shrek-frame)
![Docker Pulls](https://img.shields.io/docker/pulls/kamix08/shrek)
![GitHub last commit](https://img.shields.io/github/last-commit/Kamix-08/shrek-frame)
![Static Badge](https://img.shields.io/badge/framework-flask-flat)

A simple API in Python Flask for getting a single frame from the Shrek movie.

## usage

```/get_frame?frame_number=[frame]``` to get a specific frame from the movie.

```/get_random_frame``` to get a random frame from the movie.

```/get_length``` to get the number of frames there are in the movie.

## installation

You can self-host the API with the usage of the Docker Image.

Alternatively, you can use the running instance hosted at [shrek.henior.dev](https://shrek.henior.dev).

## other information

The project is configured for the movie file to be called ```shrek.avi```, but you can change that in the source code.

The frames are returned in the ```.webp``` format.

Number of frames is returned as a ```json``` - ```{"total_frames": total_frames}```.
