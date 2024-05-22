from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .rag_system import MovieChatbot

def index(request):
    if 'conversation' in request.session:
        del request.session['conversation']
        
    bot_message = "Hello! I'm your movie recommendation bot. How can I assist you today?"
    return render(request, 'index.html', {'bot_message': bot_message})

def movie_search(request):
    user_input = request.POST.get('user_input', '')

    chatbot = MovieChatbot()

    if user_input:
        bot_response = chatbot.chat(user_input)
        
        # Extract keywords and use them to retrieve movies
        keywords = chatbot.extract_keywords(user_input)
        movies = chatbot.retriever.retrieve(keywords)
        
        # Update the conversation history
        conversation = request.session.get('conversation', [])
        conversation.append({'type': 'user', 'message': user_input})
        conversation.append({'type': 'bot', 'message': bot_response})
        request.session['conversation'] = conversation

        return render(request, 'index.html', {
            'conversation': conversation, 
            'bot_message': bot_response, 
            'movies': movies, 
            'user_input': user_input
        })
    else:
        return redirect('index')
