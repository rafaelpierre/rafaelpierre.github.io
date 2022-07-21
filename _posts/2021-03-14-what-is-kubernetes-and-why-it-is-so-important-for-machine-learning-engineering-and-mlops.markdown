---
layout:	post
title:	"What is Kubernetes and Why it is so Important for Machine Learning Engineering and MLOps"
date:	2021-03-14
canonical_url: https://mlopshowto.com/what-is-kubernetes-and-why-it-is-so-important-for-machine-learning-engineering-and-mlops-96249a7a279e
---





---

![](/img/1*0UVKsMcWAu4yPShIlMDcyg.jpeg)Source: [Unsplash](https://unsplash.com/photos/Esq0ovRY-Zs)If you follow up technology trends, data science, artificial intelligence and machine learning, chances are that you have come across with the term [**Kubernetes**](https://kubernetes.io/) (or **K8s**, its geek nickname).

Created by Google, **Kubernetes** is an open source **container orchestration** platform. The name “**Kubernetes**” comes from the [greek language](https://www.geekwire.com/2016/ever-come-kooky-kubernetes-name-heptio/), meaning “**helmsman**” or “**captain**”. But before understanding the reason for all these nautical references, we first need to address the question: what are containers?

### Why do we need containers

![](/img/1*PMdJw-dmR1fHMNFmvvdvZg.jpeg)Source: [Unsplash](https://unsplash.com/photos/XsP7GCLMWjM)**Containers** exploded in 2013 with the creation of [**Docker**](https://www.docker.com/). Their creation was motivated by a longstanding issue in **software engineering**: how to get software to run reliably when moved from one environment to another. Such environments could range from anything from **laptops**, **bare metal servers** sitting in a good old private data center or **virtual machines** in the cloud. Packaging an application into a container means that the end result of running it across any of these environments will be consistent.

This is specially critical as technology organizations shift away from **monolithic** **architecture patterns**, such as [**service oriented architecture**](https://en.wikipedia.org/wiki/Service-oriented_architecture) **(SOA)**, to more loosely coupled, [**microservices**](https://microservices.io/) based approaches such as [**service mesh**](https://martinfowler.com/articles/break-monolith-into-microservices.html) — which in itself are good candidates for another article.

### The need for container orchestrators

Containers solve a large part of the issue, but they are not enough, in that they are more of an abstraction. To get a working product, we still need a **container runtime —** an additional layer to coordinate and allocate proper resources to running containers. To solve that problem, the folks at Docker created [**containerd**](https://www.docker.com/blog/what-is-containerd-runtime/)**,** a container runtime.

*“Why not use containerd, then?”*— you might rightfully ask.Yes, you could simply spin up a virtual machine and use **Docker** or **Docker Compose** to run one or more different containers.Well, the challenge here is that as application architectures become more complex, we need to manage things such as:

* **Reliability**: our application needs to meet **performance** **standards** and yield **correct output** for a specific time
* **Availability:** our application should be **operationally available** for the desired percentage of the time
* **Scalability**: should be possible to **seamlessly scale** depending on the workload — preferably in an automated fashion
* **Continuous Deployment:** we want to deploy our changes to production in a **fast, continuous way**, without **disrupting** existing deployments.

This is where **Kubernetes** comes in.

### Meet the Helmsman

![](/img/1*D_CPDdGPOHry5qLZkyr66w.jpeg)Source: [Unsplash](https://unsplash.com/photos/aYHzEnSEH-w)Imagine that we have a **transportation business** in the **Port of Rotterdam**, and we must routinely ship multiple containers to **Port of Southampton**, in the **United Kingdom**. One way to do it would be using a simple, small ship that which is able to carry a couple of containers. It is able to move fast and take these containers from Rotterdam in a seamless fashion. However, it has the following caveats:

* It has **low autonomy**— you spend more time refuelling
* Higher chance to **sink** — along with the containers
* **Low scale** — It can only carry two containers at a time

If we instead decide to leverage an bigger, full fledged **cargo ship** to move our containers from Rotterdam to Southampton, we can do it in a much more **reliable**, **scalable** way:

* **High autonomy**— less time spent refuelling
* Less likely to **sink**
* **High scale** — Can carry hundreds of containers at once

In this basic example we can picture a simple container runtime as a the small ship, and **Kubernetes** as a full fledged cargo ship. It was created by **Google** with a [basic feature set in mind:](https://kubernetes.io/blog/2018/07/20/the-history-of-kubernetes-the-community-behind-it/)

* **Replication —**to deploy multiple instances of an application
* **Load balancing** and **service discovery —**to route traffic to these replicated containers
* Basic **health checking** and **repair —**to ensure a **self-healing system**
* **Scheduling —**to group **many machines** into a **single pool** and **distribute** work to them

The combination of these features also makes it possible to leverage some bonus aspects. Being able to easily replicate application instances also eases the task of deploying application versions without any kind of disruption — which enables for [**continuous deployment**](https://www.atlassian.com/continuous-delivery/continuous-deployment#:~:text=Continuous%20Deployment%20%28CD%29%20is%20a,cycle%20has%20evolved%20over%20time.)and more [**agile**](https://agilemanifesto.org/) **practices.**

And that’s not all. By leveraging **Kubernetes** manifests’ declarative approach for creating resources within the cluster, we are paving the way for, amongst other things, enabling self-service architectures where **data engineers**, **data scientists** and users in general can provision their own infrastructure with very low (human) effort.

### Why Kubernetes Is So Important for Machine Learning and MLOps

![](/img/1*pxj-qAfwI1hciwCKB3f3rg.jpeg)Source: [Unsplash](https://unsplash.com/photos/nfQk1YdGoNc)Recently, companies have started realising that in **machine learning**, research and development plays a huge part. But if not enough time, budget and effort is spent in properly **designing** and **deploying** machine learning systems in a **reliable, available, discoverable and efficient manner**, it becomes challenging to reap all of its benefits.

[**Keeping Your Machine Learning Models on the Right Track: Getting Started with MLflow, Part 2**  
*Learn how to use MLflow Model Registry to track, register and deploy Machine Learning Models effectively.*mlopshowto.com](https://mlopshowto.com/keeping-your-machine-learning-models-on-the-right-track-getting-started-with-mlflow-part-2-bbc980a1f8dc "https://mlopshowto.com/keeping-your-machine-learning-models-on-the-right-track-getting-started-with-mlflow-part-2-bbc980a1f8dc")[**Keeping Your Machine Learning Models on the Right Track: Getting Started with MLflow, Part 1**  
*Learn why Model Tracking and MLflow are critical for a successful machine learning project*mlopshowto.com](https://mlopshowto.com/keeping-your-machine-learning-models-on-the-right-track-getting-started-with-mlflow-part-1-f8ca857b5971 "https://mlopshowto.com/keeping-your-machine-learning-models-on-the-right-track-getting-started-with-mlflow-part-1-f8ca857b5971")[**About MLOps And Why Most Machine Learning Projects Fail — Part 1**  
*If you have been involved with Machine Learning (or you are aiming to be), you might be aware that reaping the…*mlopshowto.com](https://mlopshowto.com/about-mlops-and-why-most-machine-learning-projects-fail-part-1-6a4d76e84e86 "https://mlopshowto.com/about-mlops-and-why-most-machine-learning-projects-fail-part-1-6a4d76e84e86")By thinking of machine learning systems with an engineering mindset, it becomes clear that **Kubernetes** is a good match to achieve the aforementioned reliability, availability and time-to-market challenges. Kubernetes helps adopting the main principles of [**MLOps**](https://cloud.google.com/solutions/machine-learning/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning), and by doing that we are increasing the chances that our machine learning systems will provide the expected value after all the investment made in the research, development and design steps.

Finally, there is also a secondary aspect which is related to the current **MLOps** ecosystem which builds upon **Kubernetes —** with existing tools and frameworks such as [**Kubeflow**](https://www.kubeflow.org/), [**Pachyderm**](https://www.pachyderm.com/)**,** [**Argo**](https://argoproj.github.io/projects/argo/)and[**Seldon**](https://www.seldon.io/)having been created to address common MLOps challenges as examples.

### Like with everything in life, it is not all fun and games

Conceptualizing and implementing a Kubernetes architecture does not happen from one day to the other, and managing Kubernetes clusters comes with additional responsibilities, namely in terms of **governance, security, support, maintenance and costs —**critical components which are also good topics for a next article.



