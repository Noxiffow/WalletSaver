from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import auth, categories, transactions
from app.db.database import engine
from app.models import user, category, transaction

# Create database tables
user.Base.metadata.create_all(bind=engine)
category.Base.metadata.create_all(bind=engine)
transaction.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Wallet Saver API",
    description="A professional FastAPI application for managing transactions and categories with JWT authentication",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify actual origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth.router, prefix="/auth", tags=["authentication"])
app.include_router(categories.router, prefix="/categories", tags=["categories"])
app.include_router(transactions.router, prefix="/transactions", tags=["transactions"])


@app.get("/")
async def root():
    """Root endpoint with API information."""
    return {
        "message": "Wallet Saver API",
        "version": "1.0.0",
        "docs": "/docs",
        "redoc": "/redoc"
    }


@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "healthy"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)