# 🐳 Week 18 - Day 1: Docker Fundamentals
## Speaker Notes & Teaching Guide

**Total Duration:** ~3 hours (180 minutes)
- Slides + Discussion: ~60 minutes
- Hands-on Notebook: ~100 minutes  
- Challenge + Q&A: ~20 minutes

---

## 📋 Pre-Class Preparation

### Instructor Setup:
- [ ] Verify Docker Desktop is installed on teaching machine
- [ ] Test all commands in notebook beforehand
- [ ] Prepare backup slides (PDF) in case of technical issues
- [ ] Have Docker Hub open in browser
- [ ] Prepare simple troubleshooting guide for students
- [ ] Set up screen sharing for terminal demonstrations

### Student Prerequisites Check:
- [ ] Docker Desktop installed (Windows/Mac) or Docker Engine (Linux)
- [ ] Terminal access
- [ ] Week 17 FastAPI knowledge refreshed
- [ ] Text editor ready (VS Code recommended)

---

## 🎯 Learning Objectives

By the end of this session, students will:
1. ✅ Understand what Docker is and the problems it solves
2. ✅ Differentiate between Docker images and containers
3. ✅ Execute essential Docker commands confidently
4. ✅ Run and manage containers
5. ✅ Create basic Dockerfiles
6. ✅ Containerize a simple application

---

## 📊 Slide-by-Slide Teaching Guide

### **Slide 1: Title Slide**
**Duration:** 2 minutes

#### Key Points to Emphasize:
- This is Week 18 - we're entering deployment phase
- Docker is THE industry standard for containerization
- Skills learned today directly apply to production deployments
- This connects Week 17 (FastAPI) to Week 20 (AWS deployment)

#### Teaching Approach:
**Start with:** "Who has heard of Docker? Who has used it?" (gauge experience level)

**Hook:** "Have you ever said 'But it works on my machine!' when your code breaks in production? Docker solves that problem once and for all."

#### Transition:
"Before we learn Docker, we need to understand the problem it solves. Let's look at why deployment is so challenging..."

---

### **Slide 2: The Deployment Problem**
**Duration:** 5 minutes

#### Key Points to Emphasize:
- These are REAL problems every developer faces
- "Works on my machine" is a common pain point
- Environment differences cause 70% of deployment failures
- This isn't just a beginner problem - happens in professional teams

#### Teaching Approach:
**Start with:** "Raise your hand if you've experienced any of these problems..."

**Story Time:** Share a personal anecdote:
"Last year, a company spent 3 days debugging a production issue. Turned out the dev environment had Python 3.10, production had 3.8. One line of code used a 3.10-only feature. Docker would have caught this immediately."

#### Questions to Ask Students:
- "What happens when your laptop runs macOS but production runs Linux?"
- "How do you ensure everyone on your team has the same Python version?"
- "What if two projects need different versions of the same library?"

#### Common Student Confusions:
- **"Can't virtual environments solve this?"** → Yes, partially. But virtual envs don't handle system-level dependencies, OS differences, or service dependencies (databases, Redis, etc.)

#### Demonstration:
Show `python --version` on your machine, then explain how this could differ in production.

#### Time Allocation: 5 minutes
- Problem explanation: 3 minutes
- Student interaction: 2 minutes

---

### **Slide 3: Real-World Scenario**
**Duration:** 4 minutes

#### Key Points to Emphasize:
- This conversation happens daily in tech companies
- Docker bridges the gap between developers and DevOps
- The developer isn't wrong, the DevOps engineer isn't wrong - the system is broken

#### Teaching Approach:
**Act it out:** Use different voices for the developer vs DevOps engineer (makes it memorable)

**Developer voice:** (excited) "I've built this amazing ML API..."
**DevOps voice:** (stressed) "Great, but..."

#### Questions to Ask Students:
- "Why is this so frustrating for both people?"
- "Who has experienced miscommunication like this in group projects?"
- "What information would help bridge this gap?"

#### Key Insight to Drive Home:
"Docker solution: Package EVERYTHING together. The developer ships a complete, tested environment. The DevOps engineer gets a guaranteed-to-work package. Everyone's happy."

#### Transition:
"So what exactly IS Docker? Let's get a proper definition..."

---

### **Slide 4: What is Docker? (DEFINITION)**
**Duration:** 8 minutes

#### Key Points to Emphasize:
- This is the CORE concept - make sure everyone understands
- Containers ≠ virtual machines (we'll cover this next)
- "Runs consistently across any environment" is the key benefit
- The shipping container analogy is powerful

#### Teaching Approach:
**Read the definition slowly:** Give students time to process it.

**Shipping Container Analogy:**
"Before shipping containers, moving goods was chaos. Different trucks, ships, trains - everything needed different loading methods. Shipping containers standardized everything. Docker does this for software."

**Visual Walkthrough:**
Point to each step (Package → Ship → Run):
1. "Package: Put your code, Python, libraries, everything in a box"
2. "Ship: Send that box via Docker Hub (like GitHub for containers)"
3. "Run: Anyone can run that box, anywhere, same result every time"

#### Live Demo Opportunity:
"Let's see this in action..." (transition to hands-on)

#### Questions to Ask Students:
- "What's in a Docker container for a FastAPI app?" (code, Python, FastAPI, uvicorn, models)
- "How is this different from just sending your code file?" (dependencies, environment)

#### Common Student Confusions:
- **"Is Docker like a VM?"** → We'll cover this in the next slide, but briefly: No. Containers are much lighter.
- **"Do I need Docker if I use virtual environments?"** → Yes! Virtual envs don't handle OS differences or system dependencies.

#### Time Allocation: 8 minutes
- Definition explanation: 3 minutes
- Analogy: 2 minutes
- Package → Ship → Run walkthrough: 3 minutes

---

### **Slide 5: Containers vs VMs**
**Duration:** 7 minutes

#### Key Points to Emphasize:
- Containers are NOT baby VMs - completely different technology
- Containers share host OS kernel = huge efficiency gain
- VMs have their place (strong isolation) but containers are better for microservices
- Size difference is dramatic: GBs vs MBs

#### Teaching Approach:
**Comparison Method:** Go through each point, VM then Container

**Visual Aid:** Draw on whiteboard if available:
```
VM Architecture:
Hardware → OS → Hypervisor → [VM1 with full OS] [VM2 with full OS]

Container Architecture:
Hardware → OS → Docker Engine → [Container1] [Container2] [Container3]
```

#### Key Differences Table Discussion:
Go through each row:
- **Size:** "VM image: 2GB download. Container: 100MB. Which would you rather deploy?"
- **Boot time:** "VM: Make coffee while it boots. Container: Before you can blink."
- **Resource use:** "Run 5 VMs? You need serious hardware. Run 50 containers? Laptop handles it."

#### Questions to Ask Students:
- "When might you still want to use VMs?" (Strong isolation, running different OS kernels, legacy systems)
- "For your Week 17 FastAPI project, VM or container?" (Container!)

#### Common Student Confusions:
- **"Are containers less secure?"** → They share the kernel, so isolation isn't as strong as VMs. For most applications, container isolation is sufficient. Highly sensitive workloads might need VMs.
- **"Can I run Windows containers on Linux?"** → No. Containers share the host OS kernel. Windows containers need Windows host, Linux containers need Linux host. (Mac Docker Desktop runs a Linux VM under the hood.)

#### Demonstration Idea:
Show `docker stats` to demonstrate how little resources containers use compared to VMs (if you have time).

#### Time Allocation: 7 minutes
- Comparison walkthrough: 4 minutes
- Student questions: 2 minutes
- Summary: 1 minute

#### Transition:
"Now that we understand WHAT containers are, let's look at HOW Docker actually works..."

---

### **Slide 6: Docker Architecture**
**Duration:** 6 minutes

#### Key Points to Emphasize:
- Docker has multiple components working together
- Client-server architecture (like Git)
- Understanding this helps with troubleshooting
- Images and containers are fundamentally different things

#### Teaching Approach:
**Top-Down Explanation:**
Start with what students see (`docker` command) and work down to daemon.

**For each component:**

1. **Docker Client (CLI):**
   - "This is what YOU use. The `docker` command."
   - "It's just sending instructions to the daemon via REST API."
   - Demo: `docker version` shows client AND server versions

2. **Docker Daemon:**
   - "The actual engine. Runs in background."
   - "Does the heavy lifting: builds images, runs containers."
   - "If daemon isn't running, nothing works."

3. **Docker Images:**
   - "Templates. Blueprints. Recipes."
   - "Read-only. Never change."
   - "Think of them like a class in OOP."

4. **Docker Containers:**
   - "Running instances of images."
   - "Like objects created from a class."
   - "Where your code actually executes."

5. **Docker Hub:**
   - "Like GitHub, but for container images."
   - "Millions of pre-built images available."
   - "Also where you'll share YOUR images."

#### Analogy:
"Docker Client = steering wheel, Docker Daemon = engine, Images = car blueprints, Containers = actual cars driving, Docker Hub = car dealership."

####

 Questions to Ask Students:
- "If you type `docker run nginx`, what happens behind the scenes?" (Client → Daemon → Check local images → Pull from Hub if needed → Create container → Start it)
- "Where does the container actually run?" (On the Docker daemon, not in the client)

#### Common Student Confusions:
- **"Do I need Docker Hub to use Docker?"** → No, you can build and run images locally. Docker Hub is for sharing.
- **"Can I have multiple daemons?"** → Technically yes (Docker Swarm), but for learning, assume one daemon.

#### Troubleshooting Prep:
"If you see 'Cannot connect to Docker daemon' error, it means the background service isn't running. On Mac/Windows: start Docker Desktop. On Linux: `sudo systemctl start docker`."

#### Time Allocation: 6 minutes
- Component explanation: 4 minutes
- Q&A: 2 minutes

---

### **Slide 7: Docker Images Explained (DEFINITION)**
**Duration:** 6 minutes

#### Key Points to Emphasize:
- Images are immutable (this is CRUCIAL)
- Tags are version control for images
- Popular images are battle-tested by millions
- Layer concept will be explained more in Slide 9

#### Teaching Approach:
**Start with definition:** Read it carefully, emphasize "read-only" and "everything needed."

**Properties Walkthrough:**
Go through each property card:

1. **Immutable:**
   - "Once built, NEVER changes. Want changes? Build a new image."
   - "This guarantees reproducibility."

2. **Layered:**
   - "Images are built in layers, like a cake."
   - "Each Dockerfile instruction = new layer."
   - "More on this in Slide 9."

3. **Shareable:**
   - "Push to Docker Hub, anyone can pull."
   - "Your team pulls same image = identical environments."

4. **Versioned:**
   - "Tags = versions. `python:3.11` vs `python:3.10`."
   - "NEVER use `latest` in production! Always specific tags."

#### Popular Images Discussion:
"Let's look at the most downloaded images..."

- **python:3.11:** "Official Python foundation. Start here for Python apps."
- **nginx:latest:** "Web server. 100+ million pulls. Industry standard."
- **postgres:15:** "Database. Version 15 is the tag."
- **ubuntu:22.04:** "Bare Ubuntu OS. Build your own custom environments."

#### Recipe Analogy Explanation:
"The recipe (image) doesn't change. You can bake the same cake (container) multiple times. Same recipe, multiple cakes. Same image, multiple containers."

#### Docker Hub Demo:
If time permits, show Docker Hub in browser:
- Search for `python`
- Show official vs community images
- Point out download counts
- Show tags tab

#### Questions to Ask Students:
- "If I run `docker run python:3.11` twice, do I download the image twice?" (No, Docker caches it locally)
- "What's the difference between `nginx` and `nginx:1.25`?" (First uses latest tag, second is specific version)

#### Common Student Confusions:
- **"Can I edit an image?"** → No! Images are read-only. You create a new image based on an old one.
- **"Do I always need to download from Docker Hub?"** → No, you can build your own images locally.

#### Time Allocation: 6 minutes
- Definition + properties: 3 minutes
- Popular images: 2 minutes
- Analogy + Q&A: 1 minute

---

### **Slide 8: Docker Containers (DEFINITION)**
**Duration:** 6 minutes

#### Key Points to Emphasize:
- Containers are instances of images (OOP analogy works well)
- Containers have lifecycle states
- Stopped containers still exist (common confusion point)
- Key difference recap: Image = template, Container = running instance

#### Teaching Approach:
**Definition First:** Read slowly, emphasize "runnable instance" and "isolated environments."

**OOP Analogy:**
```python
class Dog:  # Image
    def bark(self): pass

fido = Dog()  # Container 1
rover = Dog()  # Container 2
# Same class (image), different instances (containers)
```

**Container Lifecycle Walkthrough:**
Use the visual on slide, explain each state:

1. **CREATED:** "Container exists but hasn't started yet. Like a car with engine off."

2. **RUNNING:** "Container is executing. Your app is live. Like a car driving."

3. **PAUSED:** "Temporarily frozen. Process paused but not stopped. Rare in practice."

4. **STOPPED:** "Container exited but still exists on disk. Like a parked car."

5. **DELETED:** "Gone forever. Like scrapping a car."

#### State Transition Examples:
- "Created → Running: `docker start`"
- "Running → Stopped: `docker stop` or app crashes"
- "Stopped → Running: `docker restart`"
- "Stopped → Deleted: `docker rm`"

#### Key Difference Emphasis:
"📌 REMEMBER: Images are templates (never run). Containers are instances (run and execute)."

**Visual Example:**
"One `nginx` image can spawn 10 nginx containers, each running independently, serving different websites, on different ports."

#### Questions to Ask Students:
- "If I delete a container, does the image get deleted?" (No!)
- "If I stop a container, can I restart it later?" (Yes!)
- "What happens to data inside a container when you delete it?" (Gone forever, unless using volumes - cover in Day 2)

#### Common Student Confusions:
- **"Do containers share data?"** → Not by default. Each container is isolated. (Volumes allow sharing - Day 2 topic)
- **"If I change code in a running container, does the image change?"** → NO! Image is immutable. Changes in container are lost when container is deleted (unless you commit them to a new image).

#### Demonstration Note:
"We'll see this lifecycle in action in the hands-on notebook."

#### Time Allocation: 6 minutes
- Definition: 1 minute
- Lifecycle explanation: 3 minutes
- Analogies + Q&A: 2 minutes

---

### **Slide 9: How Docker Images Work: Layers**
**Duration:** 5 minutes

#### Key Points to Emphasize:
- Layers are why Docker is so efficient
- Each Dockerfile instruction = one layer
- Layers are cached and shared
- Order matters for build performance

#### Teaching Approach:
**Visual Walkthrough:**
Point to the layer stack:
"Let's build a FastAPI app image, layer by layer..."

1. **Layer 1 (Base OS):** "Ubuntu. Big layer, ~100MB. But downloaded once, shared by all images that use Ubuntu."

2. **Layer 2 (Python Runtime):** "Python 3.11. ~50MB. Again, shared across all Python 3.11 images you build."

3. **Layer 3 (Dependencies):** "FastAPI, numpy, etc. ~30MB. If requirements.txt doesn't change, this layer is reused."

4. **Layer 4 (Your Code):** "Your app.py. ~1MB. Changes frequently, but only this layer rebuilds."

**Why Layers Matter Section:**
Go through each benefit:

1. **Caching:**
   - "Docker caches each layer. If Layer 1-3 unchanged, skip rebuilding them."
   - "Change code? Only Layer 4 rebuilds. Saves TONS of time."

2. **Sharing:**
   - "10 Python apps? All share the same Python base layer."
   - "Saves disk space. 10 apps don't take 10x space."

3. **Efficiency:**
   - "Only download/upload what changed."
   - "Push new code? Only Layer 4 uploads, not the whole 500MB image."

4. **Version Control:**
   - "Each layer has a hash. Track exactly what changed."

#### Pro Tip Explanation:
"Put things that change RARELY at bottom (base OS, Python). Put things that change FREQUENTLY at top (your code)."

**Bad Example:**
```dockerfile
COPY . .           # Your code (changes often)
RUN pip install ...  # Dependencies (changes rarely)
```
**Good Example:**
```dockerfile
RUN pip install ...  # Dependencies first
COPY . .           # Code last
```

"Why? If you change code, good example only rebuilds last layer. Bad example rebuilds everything!"

#### Questions to Ask Students:
- "If I change one line in app.py, does Docker rebuild the Python layer?" (No!)
- "Why put COPY requirements.txt before COPY app.py?" (Requirements change less often)

#### Common Student Confusions:
- **"Do I need to understand layers to use Docker?"** → Basic understanding helps, but Docker handles it automatically.
- **"Can I see the layers?"** → Yes! `docker history <image>` shows all layers.

#### Time Allocation: 5 minutes
- Layer concept: 2 minutes
- Why it matters: 2 minutes
- Best practices: 1 minute

---

### **Slide 10: Essential Docker Commands**
**Duration:** 7 minutes

#### Key Points to Emphasize:
- These 9 commands are 90% of what you'll use daily
- Practice these until they're muscle memory
- Commands follow logical patterns (verb-noun)
- Always use `--help` when unsure

#### Teaching Approach:
**Command Categories:**
Explain that commands are organized by what they operate on.

**Image Commands:**
1. **`docker pull python:3.11`**
   - "Downloads image from Docker Hub."
   - "Like `git clone` but for images."
   - Demo: Show the download progress bars

2. **`docker images`**
   - "Lists all images on your machine."
   - "Like `ls` for images."
   - "Pay attention to SIZE column - some images are huge!"

3. **`docker rmi image_id`**
   - "Remove/delete an image."
   - "Warning: Can't delete if containers are using it."

**Container Run Commands:**
4. **`docker run nginx`**
   - "Creates AND starts a container."
   - "Most important command. Many options (we'll practice)."

5. **`docker ps`**
   - "Process status. Shows RUNNING containers."
   - "Like `ps` or Task Manager for containers."

6. **`docker ps -a`**
   - "Shows ALL containers (running + stopped)."
   - "Use this to find stopped containers."

**Container Management Commands:**
7. **`docker stop container_id`**
   - "Gracefully stops a running container."
   - "Gives container 10 seconds to shut down cleanly."

8. **`docker start container_id`**
   - "Restarts a stopped container."
   - "Unlike `run`, doesn't create a new container."

9. **`docker rm container_id`**
   - "Permanently deletes a stopped container."
   - "Warning: Can't delete running containers (stop first)."

#### Pattern Recognition:
"Notice the patterns:"
- `docker <verb> <noun>`: pull image, run container, stop container
- Images and containers have DIFFERENT commands (images/rmi vs ps/rm)

#### Pro Tip About `--help`:
"Every Docker command supports `--help`. Forgot syntax? Try `docker run --help`. You'll see ALL options."

#### Live Demo Opportunity:
If time permits, quickly demo:
```bash
docker pull alpine
docker images alpine
docker run alpine echo "Hello!"
docker ps -a
```

#### Questions to Ask Students:
- "What's the difference between `docker run` and `docker start`?" (run creates new container, start restarts existing)
- "How do I see stopped containers?" (`docker ps -a`)

#### Common Student Confusions:
- **"`docker ps` shows nothing, but I just ran a container!"** → Container probably exited immediately. Use `docker ps -a`.
- **"Do I use image ID or image name?"** → Both work! Names are easier to read.

#### Time Allocation: 7 minutes
- Command explanation: 5 minutes
- Patterns + tips: 2 minutes

---

### **Slide 11: Docker Workflow: From Image to Container**
**Duration:** 5 minutes

#### Key Points to Emphasize:
- This is the complete workflow
- Each step depends on previous step
- Understanding this workflow helps with troubleshooting
- Example uses real commands

#### Teaching Approach:
**Workflow Walkthrough:**
Point to each step:

1. **FIND IMAGE:**
   - "First, search Docker Hub for what you need."
   - "Search bar at hub.docker.com."
   - "Look for 'official image' badge."

2. **PULL IMAGE:**
   - "`docker pull` downloads it."
   - "Docker caches it locally."
   - "Only happens once (unless you want to update)."

3. **RUN CONTAINER:**
   - "`docker run` creates a container from the image."
   - "This is where your app starts executing."

4. **MANAGE:**
   - "Start, stop, inspect, debug, delete."
   - "Containers are disposable. Delete and recreate freely."

**Example Workflow Explanation:**
Walk through the example:

```bash
docker pull nginx:latest
```
"Downloads nginx web server image."

```bash
docker run -d -p 8080:80 nginx
```
"Creates container, runs in background (-d), maps port 8080 to 80 (-p)."

```bash
docker ps
```
"Checks it's running."

#### Flags Explanation:
- **`-d`:** "Detached mode. Runs in background. Without it, terminal would be blocked."
- **`-p 8080:80`:** "Port mapping. Host port 8080 → Container port 80. Access via localhost:8080."

#### Real-World Context:
"This is exactly what you'll do in production:"
1. Find the right base image (python, node, nginx)
2. Pull it
3. Run your container with proper ports
4. Manage it (stop, restart, check logs)

#### Questions to Ask Students:
- "Why do we need port mapping?" (Containers are isolated. Need to expose ports to host.)
- "What if I forget to pull an image before running?" (Docker pulls automatically!)

#### Common Student Confusions:
- **"Do I always need -p?"** → Only if container runs a service that needs external access (web server, API). Command-line tools don't need it.
- **"What if port 8080 is already in use?"** → Use different port: `-p 9000:80`

#### Time Allocation: 5 minutes
- Workflow explanation: 3 minutes
- Example walkthrough: 2 minutes

---

### **Slide 12: Summary & Next Steps**
**Duration:** 4 minutes

#### Key Points to Emphasize:
- Reinforce the main concepts
- Preview what's coming next
- Transition to hands-on practice
- Build excitement for the project

#### Teaching Approach:
**Key Takeaways Review:**
Go through each checkmark:

1. "Docker packages apps + dependencies → consistent environments"
   - "No more 'works on my machine' problems!"

2. "Images = templates, Containers = instances"
   - "Like classes and objects. One image, many containers."

3. "Containers are lightweight, fast, portable vs VMs"
   - "GBs → MBs, minutes → seconds."

4. "Image layers = efficiency and caching"
   - "Only rebuild what changed."

5. "Master basic commands: pull, run, ps, stop, rm"
   - "These 5 commands get you 90% of the way."

**Quick Poll:**
"Raise your hand if you feel confident about:"
- What Docker is? (should be 100%)
- Difference between image and container? (should be 90%+)
- Basic commands? (should be 70%+)

If less than these percentages, briefly review that topic.

**What's Coming Up:**
"Tomorrow and rest of the week:"

- **Day 2:** "Writing your own Dockerfiles. Build custom images for ML projects."
- **Day 3:** "CI/CD with GitHub Actions. Automate everything!"
- **Week Project:** "Containerize your Week 17 FastAPI app. Deploy it properly."

**Transition to Hands-On:**
"Theory is done! Now let's get our hands dirty. Open the Jupyter notebook..."

#### Motivation:
"Docker skills are in TOP 10 most in-demand tech skills. What you learn today directly translates to job interviews and real projects."

#### Questions to Ask Students:
- "Any concepts still unclear before we start practicing?"
- "Who's excited to containerize their FastAPI app?"

#### Time Allocation: 4 minutes
- Takeaways review: 2 minutes
- Next steps preview: 1 minute
- Motivation + transition: 1 minute

---

## 📓 Hands-On Notebook Session

**Duration:** 100 minutes

### Session Structure:

#### Part 1-3: Installation & First Containers (25 minutes)
- Students verify Docker installation
- Run hello-world
- Pull and list images
- **Common Issues:**
  - Docker Desktop not running (have troubleshooting slide ready)
  - Permission issues on Linux (add user to docker group)
  - Slow downloads (prepare offline images if possible)

#### Part 4-5: Container Management (30 minutes)
- Run nginx container
- Practice ps, logs, stop, start, rm
- Interactive containers (terminal-based)
- **Teaching Tips:**
  - Walk through port mapping carefully
  - Show browser access to nginx
  - Demonstrate logs in real-time

#### Part 6-7: Volumes & Dockerfiles (30 minutes)
- Create Python script
- Mount volumes
- Write first Dockerfile
- Build and run custom image
- **Key Points:**
  - Volume syntax can be confusing (draw diagram)
  - Dockerfile instructions explained line-by-line
  - Emphasize layer caching

#### Part 8-9: Cleanup & Challenge (15 minutes)
- Practice cleanup commands
- Introduce beginner challenge
- Students start working independently

---

## 🎯 Beginner Challenge Guidance

**Duration:** 20 minutes

### Challenge Overview:
Students containerize a simple ML API with endpoints:
- `GET /`: Welcome
- `POST /predict`: Simple computation
- `GET /model-info`: Metadata

### Teaching Approach:

**Scaffolding:**
1. "Start with the Python code. Make sure it works locally first."
2. "Create requirements.txt with exact versions."
3. "Write Dockerfile step-by-step. Test after each instruction."
4. "Build the image. Fix errors if any."
5. "Run container. Test with curl."

**Common Mistakes to Watch For:**
- Forgetting to expose port in Dockerfile
- Wrong CMD syntax
- Missing dependencies in requirements.txt
- Not mapping ports when running container

**Hints to Give:**
- "If build fails, read error message carefully. Usually a typo."
- "Test your app locally first (without Docker)."
- "Use `docker logs` if container crashes."

**Solution Walkthrough** (if needed):
Only show solution if students are really stuck after 15 minutes.

---

## 💡 Troubleshooting Common Issues

### Issue 1: "Cannot connect to Docker daemon"
**Solution:**
- Mac/Windows: Start Docker Desktop
- Linux: `sudo systemctl start docker`
- Check: `docker version` should show client AND server

### Issue 2: "Permission denied" (Linux)
**Solution:**
```bash
sudo usermod -aG docker $USER
newgrp docker
```

### Issue 3: Container exits immediately
**Solution:**
- Check logs: `docker logs <container_id>`
- Likely: command finished (e.g., `echo "hello"` exits instantly)
- Use `-it` for interactive or `-d` with long-running process

### Issue 4: "Port already in use"
**Solution:**
- Check what's using port: `sudo lsof -i :8080` (Mac/Linux)
- Use different port: `-p 9000:80` instead of `-p 8080:80`

### Issue 5: Image build fails
**Solution:**
- Check Dockerfile syntax
- Verify file paths (COPY commands)
- Check network (can't download dependencies?)
- Try building with `--no-cache` flag

---

## 📚 Additional Resources for Students

### Documentation:
- [Docker Official Docs](https://docs.docker.com/)
- [Docker Hub](https://hub.docker.com/)
- [Dockerfile Reference](https://docs.docker.com/engine/reference/builder/)

### Practice:
- [Play with Docker](https://labs.play-with-docker.com/) - Online Docker playground
- [Docker Curriculum](https://docker-curriculum.com/) - Comprehensive tutorial

### Cheat Sheets:
- Docker Command Cheat Sheet (share PDF)
- Dockerfile Best Practices (share link)

---

## 🎓 Assessment Criteria

Students successfully completed Day 1 if they can:
- [ ] Explain what Docker is in their own words
- [ ] Differentiate between images and containers
- [ ] Pull and run a pre-built image
- [ ] List running and stopped containers
- [ ] Stop, start, and remove containers
- [ ] Create a basic Dockerfile
- [ ] Build and run a custom image
- [ ] Map ports correctly
- [ ] Troubleshoot basic Docker errors

---

## 🔄 Post-Session Follow-Up

### Homework Assignment:
"Before Day 2, containerize a simple Python script of your choice. Share your Dockerfile in Slack."

### Preview for Day 2:
"Tomorrow we'll write advanced Dockerfiles specifically for ML projects. We'll cover multi-stage builds, optimization, and Docker Compose."

### Collect Feedback:
Quick survey:
1. Pace: Too fast / Just right / Too slow?
2. Clearest concept today?
3. Most confusing concept today?
4. Ready for Day 2?

---

## 📝 Instructor Self-Reflection

After class, review:
- [ ] Did all students successfully run their first container?
- [ ] Which slide took longer than planned?
- [ ] What questions came up repeatedly?
- [ ] Any technical issues that need prep for next time?
- [ ] Did the challenge difficulty match skill level?

---

**End of Speaker Notes**

**Total Time Check:**
- Slides: 60 minutes ✅
- Notebook: 100 minutes ✅  
- Challenge: 20 minutes ✅
- **Total: 180 minutes (3 hours)** ✅

Good luck! 🐳🚀
