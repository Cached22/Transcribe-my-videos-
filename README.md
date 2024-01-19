Timeline Website
This is a simple vertical timeline website built with SvelteKit and Supabase. The timeline animates as the user scrolls down the page, with elements appearing on both the left and right sides of the line in an alternating style. Each element has a title, description, date, and an icon that describes its use.

Tech Stack
SvelteKit
Supabase for database
Design
The design is clean and simple, with a two-color theme system that users can switch between.

Local Development Setup
Follow these steps to set up the development environment locally:

Clone the repository to your local machine.
git clone <repository-url>
Navigate to the project directory.
cd timeline-website
Install the necessary dependencies.
npm install
Create a .env file in the root directory of the project and add your Supabase URL and public anon key.
SUPABASE_URL=your-supabase-url
SUPABASE_ANON_KEY=your-supabase-anon-key
Start the development server.
npm run dev
Now, you can open your browser and navigate to http://localhost:5000 to see the application running.

Note
If you encounter an error related to npm not being able to find a file, ensure that you are in the correct directory where package.json is located.
