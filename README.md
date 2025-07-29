# Movie-Recommendation-System

### Project Title:  
**Movie Recommendation System**

---

### Objective:  
The objective of this project is to build an intelligent movie recommendation system that suggests movies to users based on their preferences. The system uses machine learning techniques to analyze user behavior and movie content, providing personalized and relevant movie suggestions.

---

### Tools & Technologies Used:
- **Programming Language:** Python  
- **Libraries:** Pandas, Scikit-learn (Sklearn), Streamlit  
- **Dataset:** MovieLens dataset (commonly used for recommendation systems)

---

### Approach & Methodology:

#### 1. Data Collection and Preprocessing:  
The MovieLens dataset is used, which contains user ratings for various movies along with movie metadata (e.g., genres, titles). The data is cleaned, structured, and prepared for modeling.

#### 2. Collaborative Filtering Model:  
A collaborative filtering approach is used to recommend movies by identifying patterns in user-item interactions (ratings). This method leverages user similarities or item similarities to suggest movies that similar users have enjoyed.

#### 3. Content-Based Filtering:  
To improve recommendations, a content-based filtering component is integrated. This considers movie attributes like genres and compares them to the user’s past preferences to recommend similar movies.

#### 4. User Interface with Streamlit:  
A simple and interactive UI is developed using Streamlit. Users can input their favorite movies or rate a few movies, and the system returns the top 5 personalized movie recommendations.

#### 5. Optional Sentiment Filtering:  
Optionally, user reviews (if available) can be analyzed using sentiment analysis to further filter or adjust the recommendations based on public opinion about the movies.

---

### Deployment Steps:

1. Store all the data and code files in a single folder.  
2. Inside this folder, create a Python file named **`app.py`** containing the Streamlit app code.  
3. Open a terminal or command prompt.  
4. Navigate to the project folder using the `cd` command.  
5. Run the following command to start the app:
   ```
   streamlit run app.py
   ```
6. The browser will open and display the output of your movie recommendation system.

---

### Deliverables:
- Python Jupyter Notebook with model code and analysis  
- Streamlit-based Web App for user interaction  
- Final recommendation logic combining collaborative and content-based models

---

### Outcome:
The system effectively provides personalized movie recommendations by combining collaborative and content-based techniques, enhancing user experience and relevance. This project demonstrates the practical use of machine learning in entertainment platforms.
