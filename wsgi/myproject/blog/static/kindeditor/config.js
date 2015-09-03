KindEditor.ready(function(K) {
                K.create('#id_content',{
                	width : 700,
                	height: 400, 
                	uploadJson :'/admin/upload/kindeditor'
                });
        });