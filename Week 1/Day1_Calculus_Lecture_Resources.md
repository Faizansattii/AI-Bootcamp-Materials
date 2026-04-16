# Day 1: Calculus — Open-Source Slide & Resource Guide

**Goal:** 3-hour first lecture (≈1 hr theory + 2 hr practical) for slow learners. Everything below is free, openly licensed (Creative Commons or MIT OCW terms), and editable.

---

## 🥇 Top 3 Ready-to-Use Slide Decks (start here)

### 1. Calculus I Lecture Slides — Manifold / OpenALG (Colorado State Univ.)
- **URL:** https://alg.manifoldapp.org/projects/math1131-csu
- **Why it's the best fit:** Slides are built on top of **OpenStax Calculus** and **Active Calculus** (both CC-licensed). They include **class activities and example videos embedded per slide** — exactly what you need for a 2-hour practical block.
- **Format:** Downloadable slide decks, editable.
- **Use for:** The full 3-hour session — slides 1-X for theory, activities for practical.

### 2. MIT OpenCourseWare — 18.01SC "Single Variable Calculus"
- **URL:** https://ocw.mit.edu/courses/18-01sc-single-variable-calculus-fall-2010/
- **Specific session:** Session 1 — Introduction to Derivatives (slope of tangent line, definition) → https://ocw.mit.edu/courses/18-01sc-single-variable-calculus-fall-2010/pages/1.-differentiation/part-a-definition-and-basic-rules/session-1-introduction-to-derivatives/
- **Also grab:** Lecture Notes PDF (Fall 2006 version): https://ocw.mit.edu/courses/18-01-single-variable-calculus-fall-2006/pages/lecture-notes/
  - Lecture 1 PDF covers: Derivatives, slope, velocity, rate of change (perfect for your theory hour)
  - Lectures 3 & 4 PDFs cover: product/quotient rules, chain rule
- **License:** CC BY-NC-SA — you can edit and reuse.

### 3. Kennesaw State University — ALG Calculus Slides (Beamer/PPTX)
- **URL:** https://oer.galileo.usg.edu/mathematics-ancillary/3/ (Calc II) and the Calc I set on the same site
- **Why useful:** Clean LaTeX-Beamer slides converted to **.pptx** — so you can open them directly in PowerPoint and edit freely. The author (Lake Ritter) explicitly invites reuse.

---

## 🎯 For the "Applications to ML" part (last 15-20 min of theory)

Pure calculus courses won't cover ML optimization. Pair one of the above with:

- **MIT 18.S096 — Matrix Calculus for Machine Learning and Beyond** (IAP 2023)
  - URL: https://ocw.mit.edu/courses/18-s096-matrix-calculus-for-machine-learning-and-beyond-january-iap-2023/pages/lecture-notes/
  - **Use only the "gradient descent / why derivatives matter in ML" intuition slides** — skip the matrix-calculus depth (too hard for Day 1).
- **Stanford CS229 — Andrew Ng's notes** (gradient descent intuition, pages 4-8)
  - URL: https://cs229.stanford.edu/main_notes.pdf
  - Only use the "hillside in the fog" analogy and the gradient-descent update rule picture.
- **APXML "Introduction to Derivatives in ML"** — has the clearest beginner explanation linking derivatives → cost function → gradient descent:
  - URL: https://apxml.com/courses/calculus-essentials-machine-learning/chapter-1-calculus-ml-introduction/role-of-derivatives

---

## 📝 For the 2-hour Practical Block (exercises + worked examples)

### Paul's Online Math Notes (Lamar University) — **gold standard for practice problems**
- **URL:** https://tutorial.math.lamar.edu/classes/calci/calci.aspx
- Each topic has three levels: Notes → Practice Problems (with solutions) → Assignment Problems
- Topics you want for Day 1:
  - Derivatives — Definition and Notation
  - Interpretation of the Derivative
  - Differentiation Formulas (Power rule, Sum rule)
  - Product and Quotient Rule
  - Chain Rule
  - Optimization Problems
- **Cheat sheet** (1-page derivative rules for students to keep): https://tutorial.math.lamar.edu/ (look for "Calculus Cheat Sheet - Derivatives")

### Active Calculus (Matt Boelkins) — **best for engaging slow learners**
- **URL:** https://activecalculus.org/single/
- **Why it's perfect for your students:** The whole philosophy is "don't lecture — have students *do* calculus." Every section has short **preview activities** and **in-class activities** that build intuition step by step. Exactly right for slow learners who need to discover ideas rather than be told them.
- Free PDF and HTML, CC-BY-SA.

---

## 🗂️ Suggested 3-Hour Lesson Plan

| Time | Block | Content | Source |
|------|-------|---------|--------|
| 0:00 – 0:10 | Hook | "If you're in fog on a hill, how do you walk down?" intuition | CS229 notes / APXML |
| 0:10 – 0:25 | Concept of change & slopes | Slope of a line → slope of a curve at a point | MIT 18.01SC Session 1 |
| 0:25 – 0:45 | Derivative definition | Limit definition + "instantaneous rate of change" meaning | Manifold slides / MIT Lec 1 PDF |
| 0:45 – 1:00 | Rules of differentiation | Power, sum, product, quotient, chain (just state + 1 example each) | Paul's Online Notes / Active Calculus |
| **1:00 – 1:10** | ☕ **Break** | | |
| 1:10 – 1:25 | ML application teaser | Cost function → slope tells us which way to step → gradient descent (no math, just picture) | APXML + MIT 18.S096 intro |
| 1:25 – 2:10 | **Practical 1:** Guided worked examples | Differentiate 8-10 functions together on the board, students copy | Paul's Notes practice problems |
| 2:10 – 2:20 | ☕ **Break** | | |
| 2:20 – 2:55 | **Practical 2:** Students work in pairs | Active Calculus in-class activity sheets + 1 simple optimization problem (e.g., "maximize area of a rectangle with fixed perimeter") | Active Calculus + Paul's Notes |
| 2:55 – 3:00 | Wrap-up | Quick recap + preview of Day 2 | — |

---

## 💡 Tips for Slow, First-Time Learners

1. **Skip the formal limit definition on Day 1** if students don't know limits. Use MIT's "slope of the tangent line" picture instead. Come back to the `(f(x+h) − f(x))/h` formula only once they're comfortable with the idea.
2. **Use the same example throughout.** Pick `f(x) = x²` on slide 1 and re-use it everywhere: slope picture → definition → power rule → optimization. Reduces cognitive load.
3. **Do every differentiation rule with the same function.** E.g., differentiate `x² · sin(x)` to show product rule, then `(x² · sin(x))³` for chain rule on the board. Familiarity helps.
4. **The ML optimization example should be visual, not algebraic.** Show a picture of a bowl-shaped cost function and a ball rolling down. That's enough for Day 1.
5. **Active Calculus preview activities are your friend** — they ask students to *guess* the answer before you teach. This dramatically boosts retention for slow learners.

---

## 📦 Bonus Resources

- **GitHub — MarcToussaint/AI-lectures** (LaTeX sources for AI/ML math slides, editable): https://github.com/MarcToussaint/AI-lectures
- **OpenStax Calculus Volume 1** (free textbook, CC-BY, matches the Manifold slides): https://openstax.org/details/books/calculus-volume-1
- **LibreTexts Calculus** (remixable OER textbook): https://math.libretexts.org/Bookshelves/Calculus
- **Khan Academy — Derivatives unit** (free videos, great for students to rewatch at home): https://www.khanacademy.org/math/differential-calculus
- **3Blue1Brown — "Essence of Calculus" YouTube series** — show **Episode 1 ("The essence of calculus")** and **Episode 2 ("The paradox of the derivative")** as openers. They're the most visually intuitive 15 minutes on derivatives anywhere. Free: https://www.3blue1brown.com/topics/calculus

---

## ✅ Quickest path if you're short on time

1. Download **Manifold Calculus I slides** (base deck — 70% done).
2. Pull **2-3 extra slides** from MIT 18.01SC Session 1 on the tangent-line picture.
3. Pull **1 ML-application slide** from APXML + one picture from CS229.
4. Print **Paul's Calculus Cheat Sheet (Derivatives)** as a 1-page handout.
5. Queue **3Blue1Brown Ep. 1** (15 min) as the opening hook.

That's your full Day 1 in about 2 hours of prep.
