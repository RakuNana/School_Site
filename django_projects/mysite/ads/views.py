from django.http import HttpResponse
from django.views import View
from django.shortcuts import render, redirect, get_object_or_404 , reverse
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from ads.owner import OwnerListView, OwnerDetailView, OwnerCreateView, OwnerUpdateView, OwnerDeleteView

from ads.forms import Create_Form, CommentForm , Edit_Comments
from ads.models import Ad , Comment
# Create your views here.

class AdsListView(OwnerListView):

    model = Ad
    template_name = "ads/ad_list.html"


class AdsDetailView(OwnerDetailView):

    model = Ad
    template_name = "ads/ad_detail.html"

    def get(self, request, pk) :
        x = Ad.objects.get(id=pk)
        comments = Comment.objects.filter(ad_comment=x).order_by('-update_at')
        comment_form = CommentForm()
        context = { 'ad_comment' : x, 'comments': comments, 'comment_form': comment_form }
        return render(request, self.template_name, context)


class AdsCreateView(LoginRequiredMixin, View):

    template_name = "ads/ad_form.html"
    success_url = reverse_lazy("ads:all")

    def get(self,request, pk=None):

        form = Create_Form()
        context = {"form":form}

        return render(request, self.template_name, context)

    def post(self,request,pk=None):

        form = Create_Form(request.POST,request.FILES or None)

        if not form.is_valid():

            context = {"form": form}

            return render(request, self.template_name, context)

        picture = form.save(commit=False)
        picture.owner = self.request.user
        picture.save()
        return redirect(self.success_url)


class AdsUpdateView(OwnerUpdateView):

    template_name = "ads/ad_form.html"
    success_url = reverse_lazy("My_ads_app:all")

    def get(self, request, pk):
        picture = get_object_or_404(Ad, id=pk, owner=self.request.user)
        form = Create_Form(instance=picture)
        ctx = {'form': form}
        return render(request, self.template_name, ctx)

    def post(self, request, pk=None):
        picture = get_object_or_404(Ad, id=pk, owner=self.request.user)
        form = Create_Form(request.POST, request.FILES or None, instance=picture)

        if not form.is_valid():
            ctx = {"form": form}
            return render(request, self.template_name, ctx)

        picture = form.save(commit=False)
        picture.save()

        return redirect(self.success_url)


class AdsDeleteView(OwnerDeleteView):

    model = Ad


class CommentCreateView(LoginRequiredMixin, View):
    def post(self, request, pk) :
        f = get_object_or_404(Ad, id=pk)
        comment = Comment(text=request.POST['comment'], owner=request.user, ad_comment=f)
        comment.save()
        return redirect(reverse('My_ads_app:ad_detail', args=[pk]))


class CommentDeleteView(OwnerDeleteView):
    model = Comment
    template_name = "ads/comment_delete.html"

    # https://stackoverflow.com/questions/26290415/deleteview-with-a-dynamic-success-url-dependent-on-id
    def get_success_url(self):
        ad_comment = self.object.ad_comment
        return reverse('My_ads_app:ad_detail', args=[ad_comment.id])



def AdsPic(request,pk):
    image = get_object_or_404(Ad, id=pk)
    response = HttpResponse()
    response["Content-Type"] = image.content_type
    response["Content-Length"] = len(image.picture)
    response.write(image.picture)
    return response
