from supabase import create_client, Client

url: str = "https://bufocbnwxmyppzcwhtap.supabase.co"
key: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImJ1Zm9jYm53eG15cHB6Y3dodGFwIiwicm9sZSI6ImFub24iLCJpYXQiOjE3Mjg0NTYyMTAsImV4cCI6MjA0NDAzMjIxMH0.I5xu_RcpcZKpytCfWTq2xfFzy3_6y8rIa8ghOPMAwxY"
supabase: Client = create_client(url, key)