import pandas as pd  
import matplotlib.pyplot as plt
import seaborn as sns


csv_file = r'C:\Users\mayan\OneDrive\Desktop\casestudy\output_file.csv'
df = pd.read_csv(csv_file, usecols=['username', 'tweet', 'language', 'place', 'retweets_count', 'likes_count', 'replies_count', 'video'])


print(df.info())  
print(df.head())


if 'retweets_count' in df.columns:
    most_retweeted_user = df.loc[df['retweets_count'].idxmax(), 'username']
    print(f"The user with the most retweeted tweet is: {most_retweeted_user}")

if all(col in df.columns for col in ['retweets_count', 'likes_count', 'replies_count']):
    df['effectiveness_score'] = df['retweets_count'] * 2 + df['likes_count'] + df['replies_count']
    most_effective_tweet = df.loc[df['effectiveness_score'].idxmax()]
    print("\nMost Effective Tweet:\n", most_effective_tweet[['username', 'tweet', 'effectiveness_score']])

plt.figure(figsize=(10, 5))
df['language'].value_counts().nlargest(10).plot(kind='bar', color='skyblue')
plt.title("Top 10 Languages in Tweets")
plt.xlabel("Language")
plt.ylabel("Tweet Count")
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(10, 5))
df['place'].value_counts().nlargest(10).plot(kind='bar', color='orange')
plt.title("Top 10 Locations of Tweets")
plt.xlabel("Place")
plt.ylabel("Tweet Count")
plt.xticks(rotation=45)
plt.show()


if all(col in df.columns for col in ['retweets_count', 'likes_count', 'replies_count']):
    
    plt.figure(figsize=(8,5))
    sns.scatterplot(x=df['retweets_count'], y=df['likes_count'], alpha=0.5)
    plt.xlabel("Retweets")
    plt.ylabel("Likes")
    plt.title("Relationship Between Retweets and Likes")
    plt.show()

    plt.figure(figsize=(8,5))
    sns.scatterplot(x=df['likes_count'], y=df['replies_count'], alpha=0.5, color='red')
    plt.xlabel("Likes")
    plt.ylabel("Replies")
    plt.title("Relationship Between Likes and Replies")
    plt.show()

    plt.figure(figsize=(6,4))
    sns.heatmap(df[['retweets_count', 'likes_count', 'replies_count']].corr(), annot=True, cmap="coolwarm")
    plt.title("Correlation Between Retweets, Likes, and Replies")
    plt.show()

if 'video' in df.columns and 'likes_count' in df.columns:
    video_likes = df[df['video'] == 1]['likes_count'].mean()
    no_video_likes = df[df['video'] == 0]['likes_count'].mean()

    print(f"\nAverage likes for tweets with video: {video_likes:.2f}")
    print(f"Average likes for tweets without video: {no_video_likes:.2f}")

    # Visualization
    plt.figure(figsize=(6,4))
    sns.barplot(x=['With Video', 'Without Video'], y=[video_likes, no_video_likes], palette=['blue', 'gray'])
    plt.ylabel("Average Likes")
    plt.title("Impact of Videos on Tweet Likes")
    plt.show()