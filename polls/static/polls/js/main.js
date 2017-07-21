function updateElementIndex(el, prefix, ndx) {
    const id_regex = new RegExp('(' + prefix + '-\\d+)');
    const replacement = prefix + '-' + ndx;
    if ($(el).attr("for")) $(el).attr("for", $(el).attr("for").replace(id_regex, replacement));
    if (el.id) el.id = el.id.replace(id_regex, replacement);
    if (el.name) el.name = el.name.replace(id_regex, replacement);
}

function addForm(btn, prefix) {
    const form = $('#id_' + prefix + '-TOTAL_FORMS');
    const formCount = parseInt(form.val());
    if (formCount >= 10) {
        alert("You can't add more than 10 choices");
        return;
    }
    const row = $('.item:first').clone(true).get(0);
    $(row).removeAttr('id').insertAfter($('.item:last')).children('.hidden').removeClass('hidden');
    $(row).children().not(':last').children().each(function () {
        updateElementIndex(this, prefix, formCount);
        $(this).val('');
    });
    $(row).find('.delete-row').click(function () {
        deleteForm(this, prefix);
    });
    form.val(formCount + 1);
    return false;
}


function deleteForm(btn, prefix) {
    const form = $('#id_' + prefix + '-TOTAL_FORMS');
    const formCount = parseInt(form.val());
    if (formCount >= 10) {
        alert("Must have at least 1 choice");
        return;
    }
    $(btn).parents('.item').remove();
    const forms = $('.item');
    form.val(forms.length);
    for (let i = 0, formCount = forms.length; i < formCount; i++) {
        $(forms.get(i)).children().not(':last').children().each(function () {
            updateElementIndex(this, prefix, i);
        });
    }
    return false;
}

$(function () {
    $('.add-more').click(function () {
        return addForm(this, 'form');
    });
    $('.delete-this').click(function () {
        return deleteForm(this, 'form');
    })
});
