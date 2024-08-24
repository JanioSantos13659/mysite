
#from django.test import TestCase
#from django.contrib.auth.models import User
#from .models import Post
#from django.utils import timezone
#from datetime import timedelta

#class PostModelTest(TestCase):

  #  def setUp(self):
#        # Cria um usuário para ser o autor dos posts
#       self.user = User.objects.create_user(username='janio', password='Jose@1020')
#       # Cria um post de exemplo com timestamp atualizado
#       self.post = Post.objects.create(
#            title="Meu Primeiro Post",
#           slug="meu-primeiro-post",
#            author=self.user,
#           content="Este é o conteúdo do meu primeiro post.",
#           status=1,
#           created_on=timezone.now() - timedelta(days=2)  # Adiciona dois dias ao timestamp
#      )
##
#   def test_post_creation(self):
#       # Verifica se o post foi criado corretamente
##       self.assertEqual(self.post.slug, "meu-primeiro-post")
#       self.assertEqual(self.post.author.username, "janio")
#       self.assertEqual(self.post.content, "Este é o conteúdo do meu primeiro post.")
#       self.assertEqual(self.post.status, 1)
#
#   def test_post_ordering(self):
#      # Cria o primeiro post com um timestamp mais antigo
##       post1 = Post.objects.create(
#           title="Meu Primeiro Post",
#          slug="meu-primeiro-post-2",  # Usando um slug único
#         author=self.user,
#        content="Este é o conteúdo do meu primeiro post.",
#        status=1,
#          created_on=timezone.now() - timedelta(days=2)  # Dois dias antes
#     )
#
#       # Cria o segundo post com o timestamp atual
#        post2 = Post.objects.create(
#           #          title="Meu Segundo Post",
#          slug="meu-segundo-post",
#           author=self.user,
#           content="Este é o conteúdo do meu segundo post.",
#           status=1
#        )
#
#       posts = Post.objects.all().order_by('-created_on')
#
#     # Verifica se a ordenação está correta
#       self.assertEqual(posts[0].title, "Meu Segundo Post")
#       self.assertEqual(posts[1].title, "Meu Primeiro Post")
#
##