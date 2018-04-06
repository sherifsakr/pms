from django.conf.urls import url ,include
from project import views

#application namespace
app_name = 'ns-project'

urlpatterns = [
    # Matches any html file - to be used for gentella
    # Avoid using your .html in your resources.
    # Or create a separate django app.


    # The home page
    url(r'^dashboard/$', views.Dashboard, name='dashboard'),
    url(r'^$', views.Dashboard, name='index'),
    url(r'^$', views.Dashboard, name='dashboard'),
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^add_project/$', views.AddProject, name='add-project'),
    url(r'^project_list/$', views.ProjectList, name='project-list'),
     url(r'^project_list/(?P<project_status>\w+)$', views.ProjectList, name='project-list'),
    url(r'^project_detail/(?P<pk>\d+)$', views.ProjectDetail, name='project-detail'),
    url(r'^project_edit/(?P<pk>\d+)$', views.ProjectEdit, name='project-edit'),
    url(r'^project_delete/(?P<pk>\d+)$', views.ProjectDelete, name='project-delete'),
    url(r'^task_list_external/(?P<task_status>\w+)$', views.TaskListExternal, name='task-list-external'),
    url(r'^project_task/(?P<pk>\d+)$', views.ProjectTask, name='project-task'),
    url(r'^project_task/(?P<pk>\d+)/(?P<task_status>\w+)$', views.ProjectTask, name='project-task'),
    url(r'^project_task_detail/(?P<projectid>\d+)/(?P<taskid>\d+)$', views.ProjectTaskDetail, name='project-task-detail'),

    url(r'^task_update_start/(?P<pk>\d+)$', views.updateStartDate, name='task-update-start'),
    url(r'^update_finish_task/(?P<pk>\d+)$',views.updateTaskFinish, name='update-finish-task'),
    url(r'^update_close_task/(?P<pk>\d+)$',views.updateTaskClose, name='update-close-task'),
    url(r'^update_cancel_task/(?P<pk>\d+)$',views.updateTaskCancel, name='update-cancel-task'),
    url(r'^update_pause_task/(?P<pk>\d+)$',views.updateTaskPause, name='update-pause-task'),
    url(r'^update_assignto_task/(?P<pk>\d+)$',views.updateTaskAssignto, name='update-assignto-task'),
    url(r'^update_assignto_task/(?P<pk>\d+)/(?P<save>\w+)$',views.updateTaskAssignto, name='update-assignto-task'),
    url(r'^update_progress_task/(?P<pk>\d+)$',views.updateTaskProgress, name='update-progress-task'),
    url(r'^project_gantt/(?P<pk>\d+)$',views.ganttChart, name='project-gantt'),
    url(r'^kanban/(?P<pk>\d+)$',views.Kanban, name='kanban'),
    url(r'^project_follow_up/$',views.projectFlowUp, name='project-follow-up'),
    url(r'^project_task_delete/(?P<projectid>\d+)/(?P<taskid>\d+)$', views.ProjectTaskDelete, name='project-task-delete'),
    url(r'^project_task_edit/(?P<projectid>\d+)/(?P<taskid>\d+)$', views.ProjectTaskEdit, name='project-task-edit'),
    url(r'^project/(?P<project_id>\d+)/team$',views.ProjectTeam, name='project-team'),
    url(r'^project/(?P<project_id>\d+)/addtask$',views.AddTask, name='add-task'),
    url(r'^project/dashboard_manager$',views.DashboardManager, name='dashboard-manager'),
    url(r'^project/dashboard_pm$',views.DashboardPM, name='dashboard-pm'),
    url(r'^project/dashboard_employee/$',views.DashboardEmployee, name='dashboard-employee'),
    url(r'^project/dashboard_employee/(?P<empid>\d+)/$',views.DashboardEmployee, name='dashboard-employee'),
    url(r'^download/(?P<file_name>.+)$', views.Download, name='download'),
    url(r'^email/$', views.senmail, name='email'),
    url(r'^project_report/$', views.ProjectReport, name='project-report'),
    url(r'^project_report/(?P<selectedDpt>.+)$', views.ProjectReport, name='project-report'),
    #login from drupal
    url(r'^auth/(?P<email>.*)/(?P<signature>.*)/(?P<time>.*)/$', views.loginfromdrupal, name='loginfromdrupal'),
    #main temp
    url(r'^.*\.html', views.gentella_html, name='gentella'),
   
]
