from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm
from .models import Post
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt

# my_viewは未実装なので削除、もしくは実装してください
# @login_required
# def my_view(request):
#     # ビューの処理
#     pass

def post_list(request):
    posts = Post.objects.all().order_by('-created_at')  # 新しい順
    return render(request, 'post_list.html', {'posts': posts})

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_list')  # 投稿一覧ページへリダイレクト
    else:
        form = PostForm()
    
    return render(request, 'create_post.html', {'form': form})

def search_page(request):
    # 検索フォームの処理（GETリクエストを処理）
    keyword = request.GET.get('keyword', '')
    category = request.GET.get('category', '')
    sort = request.GET.get('sort', 'newest')

    # 投稿をフィルタリングして並び替え
    posts = Post.objects.all()

    if keyword:
        posts = posts.filter(title__icontains=keyword)  # キーワードで絞り込み
    if category:
        posts = posts.filter(category=category)  # カテゴリで絞り込み
    if sort == 'newest':
        posts = posts.order_by('-created_at')  # 新しい順
    elif sort == 'oldest':
        posts = posts.order_by('created_at')  # 古い順
    elif sort == 'likes':
        posts = posts.order_by('-likes')  # いいね数順

    # ページネーション
    paginator = Paginator(posts, 4)  # 1ページあたり10件の投稿
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'search.html', {'page_obj': page_obj})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)  # 投稿をpkで取得
    return render(request, 'post_detail.html', {'post': post})


def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    # まだ「いいね」していない場合は、いいね数を増やす
    post.likes += 1
    post.save()

    # AJAXリクエストに対するレスポンス
    return JsonResponse({
        'likes': post.likes,
    })

    # AJAXリクエストに対するレスポンス
    return JsonResponse({
        'likes': post.likes,
        'liked': liked,
    })

@csrf_exempt
def delete_post(request, post_id):
    if request.method == 'POST':
        password = request.POST.get('password')
        correct_password = 'kamakuranet'  # ここに実際のパスワードを設定

        if password == correct_password:
            # 投稿を削除
            try:
                post = Post.objects.get(id=post_id)
                post.delete()
                return JsonResponse({'success': True})
            except Post.DoesNotExist:
                return JsonResponse({'success': False, 'message': '投稿が見つかりません。'})
        else:
            return JsonResponse({'success': False, 'message': 'パスワードが間違っています。'})
    return JsonResponse({'success': False, 'message': '無効なリクエストです。'})