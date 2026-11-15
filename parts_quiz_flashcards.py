# -*- coding: utf-8 -*-

TAB_FLASHCARDS_HTML = """
<div id="flashcards" class="tab-pane">
  <div class="hero-banner">
    <div class="hero-header">
      <div class="hero-title">Interactive Cloud Computing Flashcards</div>
      <div class="hero-badge-group">
        <span class="badge badge-accent">Rapid Revision</span>
        <span class="badge">36 High-Yield Concepts</span>
      </div>
    </div>
    <p class="hero-desc">
      Master core definitions, components, and exam tricks. Click or tap any flashcard to flip between the Question and the Answer.
      Use the navigation buttons below to step through all cards.
    </p>
  </div>

  <div class="flashcard-wrapper">
    <div class="flashcard" id="activeFlashcard" onclick="flipCard()">
      <div class="flashcard-front">
        <div class="card-unit-badge" id="fcUnitBadge">Unit 1: Foundations</div>
        <div class="card-content">
          <div class="card-question" id="fcQuestion">What is Cloud Computing?</div>
        </div>
        <div class="card-hint">💡 Tap or Click to Flip for Answer</div>
      </div>
      <div class="flashcard-back">
        <div class="card-unit-badge" style="color: var(--purple);">Answer & Key Insight</div>
        <div class="card-content">
          <div class="card-answer" id="fcAnswer">
            The delivery of computing services (servers, storage, databases, networking, software, analytics) over the Internet on a pay-as-you-go basis without purchasing physical hardware.
          </div>
        </div>
        <div class="card-hint">🔄 Tap again to flip back</div>
      </div>
    </div>

    <div class="flashcard-nav">
      <button class="btn" onclick="prevCard()">◀ Previous</button>
      <span style="font-weight: 700; font-size: 0.9rem;" id="fcCounter">Card 1 of 36</span>
      <button class="btn btn-primary" onclick="nextCard()">Next ▶</button>
      <button class="btn" onclick="shuffleCards()">🔀 Shuffle</button>
    </div>
  </div>
</div>
"""

TAB_QUIZ_HTML = """
<div id="quiz" class="tab-pane">
  <div class="hero-banner">
    <div class="hero-header">
      <div class="hero-title">Cloud Computing Exam MCQ Simulator</div>
      <div class="hero-badge-group">
        <span class="badge badge-priority">52 Verified Questions (100% Syllabus)</span>
        <span class="badge" id="liveScoreBadge">Score: 0 / 0</span>
      </div>
    </div>
    <p class="hero-desc">
      Test your preparation with this realistic exam simulator. Features all 20 questions from Units 1 & 2, 12 from Unit 3, 10 from Unit 4, and 10 from Unit 5.
      Instant answers, grading, and in-depth explanations are revealed on selection.
    </p>
  </div>

  <div class="quiz-container">
    <div class="quiz-progress-bar-container">
      <div class="quiz-progress-bar" id="quizProgressBar"></div>
    </div>

    <div class="quiz-filter">
      <button class="btn btn-primary" onclick="filterQuiz('all', this)">All (52)</button>
      <button class="btn" onclick="filterQuiz('unit1', this)">Unit 1 (10)</button>
      <button class="btn" onclick="filterQuiz('unit2', this)">Unit 2 (10)</button>
      <button class="btn" onclick="filterQuiz('unit3', this)">Unit 3 (12)</button>
      <button class="btn" onclick="filterQuiz('unit4', this)">Unit 4 (10)</button>
      <button class="btn" onclick="filterQuiz('unit5', this)">Unit 5 (10)</button>
      <button class="btn" onclick="resetQuiz()">🔄 Reset</button>
    </div>

    <div id="quizQuestionsList">
      <!-- Quiz cards will be rendered dynamically by JavaScript -->
    </div>
  </div>
</div>
"""
