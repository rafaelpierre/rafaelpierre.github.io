---
layout:	post
title:	"Nevermind Docker Desktop, Here is Podman"
date:	2022-05-26
canonical_url: https://mlopshowto.com/nevermind-docker-desktop-here-is-podman-53018f23b059
---





---

![](/img/1*sGv1D57xkypPxMu9vry2rg.jpeg)### Background

**UPDATE (28/05/2022):** *Podman covers most of Docker functionality, however I found that image layer caching is currently missing. One solution is using Podman coupled with* [*buildkit*](https://pythonspeed.com/articles/podman-buildkit/)*.*

[Docker changed its license terms in August 2021](https://www.docker.com/blog/updating-product-subscriptions/ "https://www.docker.com/blog/updating-product-subscriptions/"). That means it is no longer possible to use Docker Desktop in a commercial setting without purchasing a license.

While it is possible to request a license for it, a great open source alternative is to use [Podman](https://podman.io/ "https://podman.io/").

![](/img/1*o1O3DQDMAl8WSx4y79NYqQ.png)**TLDR** from their website: *“Podman is a daemonless container engine for developing, managing, and running OCI Containers on your Linux System. Containers can either be run as root or in rootless mode. Simply put:* ***alias docker=podman****. More details* [*here*](https://podman.io/whatis.html "https://podman.io/whatis.html")*.”*

### How to install it and run it

On a macOS it’s pretty easy:


```
brew install podman
```
Once it’s installed, you need to create a virtual machine. This can be done by running:


```
podman machine init
```
This should have created a virtual machine which will be used as our backend for everything Podman related. Let’s go on and start our virtual machine with:


```
podman machine start
```
Our virtual machine should be running & ready to use. We can double check by running:


```
podman machine list
```
![](/img/1*MxXKfnIBJlI-KvCqgxYYww.png)### Usage

The Podman CLI uses the same conventions and parameters as Docker’s, which is pretty neat. You can even create an alias for it, so that you can fire it up using the good and old *docker* command. Just add the following to your *.bash\_profile (*or*.zshrc,* if you use [ZShell](https://en.wikipedia.org/wiki/Z_shell "https://en.wikipedia.org/wiki/Z_shell")):


```
alias docker=podman
```
And you’re done. You can test it quite easily by pulling an image:


```
docker pull busybox
```
### Troubleshooting

### Unable to start host networking

It could be that you come across this error when trying to start Podman’s VM (*podman machine start*):


```
Error: unable to start host networking: “could not find \”gvproxy\” in one of [/usr/local/opt/podman/libexec /opt/homebrew/bin /opt/homebrew/opt/podman/libexec 3/usr/local/bin /usr/local/libexec/podman /usr/local/lib/podman /usr/libexec/podman 4/usr/lib/podman]”
```
To solve that, from a terminal window run:


```
vim ~/.config/containers/containers.conf
```
In the **engine** section, add the following line (replace 4.1.0 with your version if needed):


```
helper\_binaries\_dir=[“/usr/local/Cellar/podman/4.1.0/bin”,”/usr/local/Cellar/podman/4.1.0/libexec”]
```
Your final *containers.conf* file should look like this:

![](/img/1*9LzOa6wO0SgAdMtcZkfUSA.png)### QEMU

[QEMU](https://www.qemu.org/ "https://www.qemu.org/") is a virtualization engine for Mac. Depending on your environment, you might also need to install it. Easy to do it with brew:


```
brew install qemu
```
Now you should be good to go 😄

### Podman Compose

You might be asking: what about [Docker Compose](https://docs.docker.com/compose/ "https://docs.docker.com/compose/")? Well, I’ve got some good news for you: there’s **Podman Compose**!

To install it:


```
pip3 install podman-compose
```
You can run it in the same way as Docker Compose. From a directory containing your *docker-compose.yam*l, simply run:


```
podman-compose up
```
Needless to say — you could also create an alias for it:


```
alias docker-compose=podman-compose
```
### Bonus: Using Podman to Migrate from Docker Compose to Kubernetes

One challenge with Docker Compose is that the YAML file format only works with the Docker engine. While you can give it to other Docker users for local replication, they cannot use it with other container runtimes. That is, until now.

There’s a nice bonus with **Podman**: you can use it to convert package the containers that you have previously spun up with Docker Compose to **Kubernetes YAML Manifests**.

To do so, simply run:


```
podman generate kube -s -f manifest_name.yaml CONTAINER_ID
```
As a result, you will get something like this:

![](/img/1*i1PENVJY-PYnGz8J5GW9AA.png)Pretty neat, huh?### You might also like

[**Keeping Your Machine Learning Models on the Right Track: Getting Started with MLflow, Part 2**  
*Learn how to use MLflow Model Registry to track, register and deploy Machine Learning Models effectively.*mlopshowto.com](https://mlopshowto.com/keeping-your-machine-learning-models-on-the-right-track-getting-started-with-mlflow-part-2-bbc980a1f8dc "https://mlopshowto.com/keeping-your-machine-learning-models-on-the-right-track-getting-started-with-mlflow-part-2-bbc980a1f8dc")[**Keeping Your Machine Learning Models on the Right Track: Getting Started with MLflow, Part 1**  
*Learn why Model Tracking and MLflow are critical for a successful machine learning project*mlopshowto.com](https://mlopshowto.com/keeping-your-machine-learning-models-on-the-right-track-getting-started-with-mlflow-part-1-f8ca857b5971 "https://mlopshowto.com/keeping-your-machine-learning-models-on-the-right-track-getting-started-with-mlflow-part-1-f8ca857b5971")[**What are Feature Stores and Why Are They Critical For Scaling Machine Learning**  
*Understand why Feature Stores are critical for a good MLOps foundation*mlopshowto.com](https://mlopshowto.com/what-are-feature-stores-and-why-are-they-critical-for-scaling-machine-learning-94e14afec81d "https://mlopshowto.com/what-are-feature-stores-and-why-are-they-critical-for-scaling-machine-learning-94e14afec81d")### Reference

[**How Podman runs on Macs and other container FAQs**  
*As the Podman machine function becomes more used-particularly on Macs-there have been many questions about how this all…*www.redhat.com](https://www.redhat.com/sysadmin/podman-mac-machine-architecture "https://www.redhat.com/sysadmin/podman-mac-machine-architecture")[**Dockerless containers with Podman on MacOS**  
*Docker the company has been throwing wrenches lately into what used to be a smooth user experience with their new Terms…*awstip.com](https://awstip.com/dockerless-containers-with-podman-on-macos-7b08a8e308fa "https://awstip.com/dockerless-containers-with-podman-on-macos-7b08a8e308fa")

