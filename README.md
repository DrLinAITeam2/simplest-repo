# Task Status Transition Demo

This project demonstrates task status transitions using a Next.js frontend and a Python FastAPI backend.

## Project Structure

- `frontend/`: Next.js application for the UI demo
- `backend/`: Python FastAPI server providing the status transition API
- `backend/states.py`: Core state machine logic
- `backend/api.py`: FastAPI endpoints
- `backend/test_api.py`: API tests

## Backend

The backend provides a REST API for task status management based on the state machine defined in `backend/states.py`.

### Installation

```bash
cd backend
pip install -r requirements.txt
```

### Running the API Server

```bash
cd backend
uvicorn api:app --reload
```

The API will be available at `http://localhost:8000`.

### API Endpoints

- `GET /statuses`: Get all possible task statuses
- `GET /transitions/{status}`: Get allowed transitions for a status
- `POST /transition`: Attempt a transition (body: `{"current": "pending", "target": "in_progress"}`)

### Running Tests

```bash
cd backend
pytest test_api.py
```

## Frontend

The frontend is a Next.js app that demonstrates the state transitions.

### Installation

```bash
cd frontend
npm install
```

### Running the Development Server

```bash
cd frontend
npm run dev
```

Open [http://localhost:3000](http://localhost:3000) with your browser to see the demo.

## CI/CD

GitHub Actions workflow runs backend tests on pushes and PRs to main.

## Getting Started

1. Set up the backend API
2. Run the frontend development server
3. Interact with the status transition demo

This is a [Next.js](https://nextjs.org) project bootstrapped with [`create-next-app`](https://nextjs.org/docs/app/api-reference/cli/create-next-app).

## Getting Started

First, run the development server:

```bash
npm run dev
# or
yarn dev
# or
pnpm dev
# or
bun dev
```

Open [http://localhost:3000](http://localhost:3000) with your browser to see the result.

You can start editing the page by modifying `app/page.tsx`. The page auto-updates as you edit the file.

This project uses [`next/font`](https://nextjs.org/docs/app/building-your-application/optimizing/fonts) to automatically optimize and load [Geist](https://vercel.com/font), a new font family for Vercel.

## Learn More

To learn more about Next.js, take a look at the following resources:

- [Next.js Documentation](https://nextjs.org/docs) - learn about Next.js features and API.
- [Learn Next.js](https://nextjs.org/learn) - an interactive Next.js tutorial.

You can check out [the Next.js GitHub repository](https://github.com/vercel/next.js) - your feedback and contributions are welcome!

## Deploy on Vercel

The easiest way to deploy your Next.js app is to use the [Vercel Platform](https://vercel.com/new?utm_medium=default-template&filter=next.js&utm_source=create-next-app&utm_campaign=create-next-app-readme) from the creators of Next.js.

Check out our [Next.js deployment documentation](https://nextjs.org/docs/app/building-your-application/deploying) for more details.