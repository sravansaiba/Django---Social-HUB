# Social Media Website (Twitter Clone)

This project is a social media website inspired by Twitter, built using Django. The platform allows users to create, read, update, and delete (CRUD) posts. Users can upload posts with or without images and interact with each other through posts and comments.

## Features

### 1. User Authentication
- **Registration:** Users can create an account.
- **Login/Logout:** Users can log in to access the platform and log out when done.
- **Password Management:** Users can reset and change their passwords.

### 2. Post Uploading
- **Text-Only Posts:** Users can create posts that contain only text.
- **Posts with Images:** Users can create posts that include both text and an image.
- **Image Handling:** Images are uploaded and stored securely, with appropriate validation for image formats and sizes.

### 3. CRUD Operations
- **Create:** Users can create new posts.
- **Read:** Users can view posts made by themselves and other users.
- **Update:** Users can edit their posts.
- **Delete:** Users can delete their posts.
- **View Details:** Each post can be clicked on to view more details.

### 4. User Profile Management
- **Profile Editing:** Users can update their profile information, including their bio and profile picture.
- **User Dashboard:** Users have a dashboard where they can see their posts and interactions.

### 5. Like and Comment System (Optional)
- **Liking Posts:** Users can like and unlike posts.
- **Commenting:** Users can comment on posts.

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/social-media-website.git
   cd social-media-website
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations:**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser:**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

7. **Access the website:**
   Open your web browser and navigate to `http://127.0.0.1:8000/`.

## Usage

- **Creating Posts:**
  - Navigate to the post creation page.
  - Enter your text in the provided field.
  - Optionally, upload an image.
  - Click the "Post" button to share your post.

- **Managing Posts:**
  - To edit or delete a post, navigate to your profile or the post's detail page.
  - Use the provided buttons to update or delete the post.

## Technologies Used

- **Backend:** Django
- **Frontend:** HTML, CSS, JavaScript
- **Database:** SQLite (default, can be changed to PostgreSQL, MySQL, etc.)
- **Other:** Bootstrap for responsive design, Pillow for image processing

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeature`).
3. Make your changes and commit them (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a Pull Request.

## Contact

For any questions, feel free to reach out via [your email address] or create an issue in the repository.
