from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'common/index.html'  # Template for the home page


class AboutView(TemplateView):
    template_name = 'common/about.html'


class BlogPostView(TemplateView):
    template_name = 'common/blog-post.html'


class ContactView(TemplateView):
    template_name = 'common/contact.html'


class ElementsView(TemplateView):
    template_name = 'common/elements.html'  # Rename to 'elements'


class RecipePostView(TemplateView):
    template_name = 'common/recipe-post.html'
