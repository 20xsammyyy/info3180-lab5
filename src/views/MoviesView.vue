<template>
    <div class="movies-container">
      <h2 class="movies-title">My Movie Collection</h2>
  
      <div v-if="movies.length === 0" class="no-movies">
        <div class="empty-state">
          <div class="icon">🎬</div>
          <p>No movies in your collection yet.</p>
        </div>
      </div>
  
      <div v-else class="movie-grid">
        <div class="movie-card" v-for="movie in movies" :key="movie.id">
          <div class="poster-container">
            <img
              :src="movie.poster"
              :alt="movie.title + ' Poster'"
              class="movie-poster"
            />
          </div>
          <div class="movie-info">
            <h3 class="movie-title">{{ movie.title }}</h3>
            <p class="movie-description">{{ movie.description }}</p>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref, onMounted } from "vue";
  
  const movies = ref([]);
  
  function fetchMovies() {
    fetch("/api/v1/movies")
      .then((response) => response.json())
      .then((data) => {
        movies.value = data.movies;
      })
      .catch((error) => {
        // console.error("Error fetching movies:", error);
      });
  }
  
  onMounted(() => {
    fetchMovies();
  });
  </script>
  
  <style scoped>
  .movies-container {
    max-width: 1100px;
    margin: 0 auto;
    padding: 2rem 1rem;
  }
  
  .movies-title {
    font-size: 2.4rem;
    font-weight: 700;
    color: #2c3e50;
    margin-bottom: 2rem;
    text-align: center;
    position: relative;
  }
  
  .movies-title::after {
    content: "";
    position: absolute;
    bottom: -10px;
    left: 50%;
    transform: translateX(-50%);
    width: 80px;
    height: 4px;
    background: linear-gradient(90deg, #3498db, #9b59b6);
    border-radius: 3px;
  }
  
  .no-movies {
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 300px;
  }
  
  .empty-state {
    text-align: center;
    padding: 2rem;
    background-color: #f1f3f5;
    border-radius: 12px;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
    width: 100%;
    max-width: 400px;
  }
  
  .empty-state .icon {
    font-size: 3.5rem;
    margin-bottom: 1rem;
    color: #9b59b6;
  }
  
  .empty-state p {
    font-size: 1.1rem;
    color: #6c757d;
  }
  
  .movie-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(260px, 1fr));
    gap: 1.8rem;
  }
  
  .movie-card {
    background-color: #ffffff;
    border-radius: 12px;
    overflow: hidden;
    box-shadow: 0 6px 18px rgba(0, 0, 0, 0.08);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    display: flex;
    flex-direction: column;
    height: 100%;
  }
  
  .movie-card:hover {
    transform: translateY(-6px);
    box-shadow: 0 10px 25px rgba(0, 0, 0, 0.12);
  }
  
  .poster-container {
    position: relative;
    padding-top: 150%; /* 2:3 aspect ratio */
    background: #f8f9fa;
  }
  
  .movie-poster {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    object-fit: cover;
    transition: transform 0.4s ease-in-out;
  }
  
  .movie-card:hover .movie-poster {
    transform: scale(1.04);
  }
  
  .movie-info {
    padding: 1.2rem 1.4rem;
    display: flex;
    flex-direction: column;
    flex-grow: 1;
  }
  
  .movie-title {
    font-size: 1.25rem;
    font-weight: 600;
    margin-bottom: 0.6rem;
    color: #2c3e50;
    line-height: 1.2;
  }
  
  .movie-description {
    font-size: 0.95rem;
    color: #555;
    line-height: 1.5;
    /* Removed the line-clamp properties to show full descriptions */
  }
  
  /* Mobile Responsiveness */
  @media (max-width: 768px) {
    .movie-grid {
      grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
      gap: 1.5rem;
    }
  
    .movies-title {
      font-size: 2rem;
    }
  }
  
  @media (max-width: 480px) {
    .movie-grid {
      grid-template-columns: 1fr;
    }
  
    .poster-container {
      padding-top: 70%; /* Adjusted aspect ratio for smaller screens */
    }
  
    .movie-title {
      font-size: 1.1rem;
    }
  
    .movie-description {
      font-size: 0.85rem;
    }
  }
  </style>