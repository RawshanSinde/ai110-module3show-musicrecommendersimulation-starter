"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv")
    print(f"Loaded songs: {len(songs)}")

    # Taste profile derived from user's actual playlist
    # (Sabrina Carpenter, Zara Larsson, Don Toliver, Tory Lanez)
    # Categorical features: exact match scoring
    # Numerical features: proximity scoring — closer to target = higher score
    user_prefs = {
        # --- Categorical features ---
        "genre":        "dance pop",   # dominant genre across playlist
        "mood":         "confident",   # upbeat, self-assured tone preferred

        # --- Numerical features (all on 0.0–1.0 scale) ---
        "energy":       0.78,          # high energy but not peak — Espresso/Can't Tame Her range
        "valence":      0.82,          # bright and positive leaning
        "danceability": 0.84,          # highly danceable tracks preferred
        "acousticness": 0.12,          # produced/electronic sound preferred over acoustic

        # --- Tempo (normalized from BPM range 60–152) ---
        # Raw target: ~110 BPM  →  normalized: (110 - 60) / (152 - 60) ≈ 0.54
        "tempo_normalized": 0.54,

        # --- Feature weights (must sum to 1.0) ---
        # Higher weight = this feature matters more in the final score
        "weights": {
            "energy":           0.25,  # most important — pace and intensity
            "mood":             0.20,  # emotional context
            "danceability":     0.20,  # core to this user's taste
            "genre":            0.15,  # style tiebreaker — meaningful but not dominant
            "valence":          0.10,  # positivity/brightness
            "acousticness":     0.10,  # preference for produced sound
        }
    }

    recommendations = recommend_songs(user_prefs, songs, k=5)

    print("\n" + "=" * 50)
    print("  TOP RECOMMENDATIONS")
    print("=" * 50)

    for rank, (song, score, explanation) in enumerate(recommendations, start=1):
        print(f"\n#{rank}  {song['title']} — {song['artist']}")
        print(f"     Score : {score:.2f} / 1.00")
        print(f"     Genre : {song['genre']}   Mood: {song['mood']}")
        print(f"     Why   :")
        for reason in explanation.split(" | "):
            print(f"             • {reason}")
        print("-" * 50)


if __name__ == "__main__":
    main()
