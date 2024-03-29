from flask import url_for
from flask_mail import Message
from flaskblog import mail
import re, sys, secrets
from email.mime.image import MIMEImage
from flaskblog.models import Project, Grant
from flaskblog.projects.forms import ProjectForm
# setting path
sys.path.append('../../flaskblog')
from flaskblog.config import get_admins
from flask_login import current_user
from flaskblog import db
from flaskblog.models import User

#Maud : 4010240
#Théo : 4079061
#Dina : 4209954
#Julien : 4177905

#user.email, #project creator
#'dina.ouahbi@aphp.fr',
def send_recap_project(user, body, form, project_id):
    token = user.get_reset_token()
    admins = [User.query.filter_by(is_admin=True).all()[i].email for i in range(len(User.query.filter_by(is_admin=True).all()))]
    msg = Message(f'Résumé de votre projet | {form.project_title.data.capitalize()} | {form.application.data.capitalize()}',
                  sender='helpbioinfo@sls.aphp.fr',
                  cc = [form.email.data],
                  recipients=[user.email, #project creator
                              'dina.ouahbi@aphp.fr',
                              'julien.robert@aphp.fr',
                              'abdeljalil.senhajirachik@aphp.fr'])
    msg.body = f"""
    Bonjour {user.username.capitalize()},

    Suite à votre demande d'aide pour le projet intitulé"{form.project_title.data.capitalize()}", 
    veuillez trouver ci-dessous un résumé des points qui résument les différents critères du projet :
                
                {body}

    Une réponse vous sera envoyée par l'équipe de bioinformatique de l'hôpital Saint-Louis dans les plus brefs délais.

    Identifiant du projet: {project_id}

    Si vous avez des questions, n'hésitez pas à revenir sur la page de contact en cliquant sur le lien ci-dessous.
                
    {url_for('main.about', token=token, _external = True)}

    Vous pouvez consulter les projets de notre équipe sur Github en cliquant sur le lien ci-dessous.

    https://github.com/bioinformatic-hub-sls


    Salutations,
    Equipe des bioinformaticiens de l'APHP - SLS, 
    """
    mail.send(msg)

def extract_label(s):
    matches = re.findall('"([^"]*)"', str(s))
    return matches[0]

#------------------------------------- PROJECT -----------------------------------------------------

def extract_form_info(form):
    body = f'''

        {extract_label(form.username.label)}\t:\t{form.username.data} \n
        {extract_label(form.application.label)}\t:\t{form.application.data} \n
        {extract_label(form.laboratories.label)}\t:\t{form.laboratories.data} \n
        {extract_label(form.if_no_laboratory.label)}\t:\t{form.if_no_laboratory.data} \n
        {extract_label(form.clinical_service.label)}\t:\t{form.clinical_service.data} \n
        {extract_label(form.organism.label)}\t:\t{form.organism.data} \n

                ***************************************

        {extract_label(form.principal_investigator.label)}\t:\t{form.principal_investigator.data} \n
        {extract_label(form.promotor.label)}\t:\t{form.promotor.data} \n
        {extract_label(form.regulatory_requirements.label)}\t:\t{form.regulatory_requirements.data} \n
        {extract_label(form.if_regulatory_requirements.label)}\t:\t{form.if_regulatory_requirements.data} \n

                ***************************************

        {extract_label(form.project_title.label)}\t:\t{form.project_title.data} \n
        {extract_label(form.urgency_of_request)}\t:\t{form.urgency_of_request.data} \n
        {extract_label(form.if_urgency.label)}\t:\t{form.if_urgency.data} \n
        {extract_label(form.project_context.label)}\t:\t{form.project_context.data} \n
        {extract_label(form.project_context_private.label)}\t:\t{form.project_context_private.data} \n

                ***************************************

        {extract_label(form.project_summary.label)}\t:\t{form.project_summary.data} \n
        {extract_label(form.bioF_needs.label)}\t:\t{form.bioF_needs.data} \n
        {extract_label(form.data_available.label)}\t:\t{form.data_available.data} \n
        {extract_label(form.access_data.label)}\t:\t{form.access_data.data} \n

                ***************************************

        {extract_label(form.data_owner.label)}\t:\t{form.data_owner.data} \n
        {extract_label(form.data_type.label)}\t:\t{form.data_type.data} \n
        {extract_label(form.data_size.label)}\t:\t{form.data_size.data} \n
        {extract_label(form.email.label)}\t:\t{form.email.data} \n
        {extract_label(form.add_info.label)}\t:\t{form.add_info.data} \n
    '''
    return body

def object_project(form):
    project = Project(
        username = form.username.data,
        email = form.email.data,
        author = current_user,
        project_token = secrets.token_bytes(32).hex(),
        project_title = form.project_title.data,
        application = form.application.data,
        organism = form.organism.data,
        principal_investigator = form.principal_investigator.data,
        promotor = form.promotor.data,
        urgency_of_request = form.urgency_of_request.data,
        if_urgency = form.if_urgency.data,
        project_context = form.project_context.data,
        project_context_private = form.project_context_private.data,
        project_summary = form.project_summary.data,
        bioF_needs = form.bioF_needs.data,
        data_available = form.data_available.data,
        access_data = form.access_data.data,
        data_owner = form.data_owner.data,
        regulatory_requirements = form.regulatory_requirements.data,
        if_regulatory_requirements = form.if_regulatory_requirements.data,
        data_type = form.data_type.data,
        data_size = form.data_size.data,
        add_info = form.add_info.data
    )

    return project

def project_update(form, project, method):
    if method == 'POST':
        project.username = form.username.data
        project.email = form.email.data
        project.project_title = form.project_title.data
        project.application = form.application.data
        project.organism = form.organism.data
        project.principal_investigator = form.principal_investigator.data
        project.promotor = form.promotor.data
        project.urgency_of_request = form.urgency_of_request.data
        project.if_urgency = form.if_urgency.data
        project.project_context = form.project_context.data
        project.project_summary = form.project_summary.data
        project.bioF_needs = form.bioF_needs.data
        project.data_available = form.data_available.data
        project.access_data = form.access_data.data
        project.data_owner = form.data_owner.data
        project.regulatory_requirements = form.regulatory_requirements.data
        project.if_regulatory_requirements = form.if_regulatory_requirements.data
        project.data_type = form.data_type.data
        project.data_size = form.data_size.data
        #project.funding_type = form.funding_type.data
        #project.total_amount = form.total_amount.data
        #project.deadline = form.deadline.data

        db.session.commit()
    elif method == 'GET':
        form.username.data = project.username
        form.email.data = project.email
        form.project_title.data = project.project_title
        form.application.data = project.application
        form.organism.data = project.organism
        form.principal_investigator.data = project.principal_investigator
        form.promotor.data = project.promotor
        form.urgency_of_request.data = project.urgency_of_request
        form.if_urgency.data = project.if_urgency
        form.project_context.data = project.project_context
        form.project_summary.data = project.project_summary
        form.bioF_needs.data = project.bioF_needs
        form.data_available.data = project.data_available
        form.access_data.data = project.access_data
        form.data_owner.data = project.data_owner
        form.regulatory_requirements.data = project.regulatory_requirements
        form.if_regulatory_requirements.data = project.if_regulatory_requirements
        form.data_type.data = project.data_type
        form.data_size.data = project.data_size

        #form.funding_type.data = project.funding_type
        #form.total_amount.data = project.total_amount
        #form.deadline.data = project.deadline

#------------------------------------- GRANT -----------------------------------------------------

def extract_form_info_grant(form):
    body = f'''

        {extract_label(form.username.label)}\t:\t{form.username.data} \n
        {extract_label(form.email.label)}\t:\t{form.email.data} \n
        {extract_label(form.project_title.label)}\t:\t{form.project_title.data} \n
        {extract_label(form.application.label)}\t:\t{form.application.data} \n
        {extract_label(form.organism.label)}\t:\t{form.organism.data} \n

                ***************************************

        {extract_label(form.principal_investigator.label)}\t:\t{form.principal_investigator.data} \n
        {extract_label(form.promotor.label)}\t:\t{form.promotor.data} \n
        {extract_label(form.funding_type.label)}\t:\t{form.funding_type.data} \n
        {extract_label(form.total_amount.label)}\t:\t{form.total_amount.data} \n
        {extract_label(form.deadline.label)}\t:\t{form.deadline.data} \n
        {extract_label(form.urgency_of_request.label)}\t:\t{form.urgency_of_request.data} \n
        {extract_label(form.if_urgency.label)}\t:\t{form.if_urgency.data} \n

                ***************************************

        {extract_label(form.project_context.label)}\t:\t{form.project_context.data} \n
        {extract_label(form.project_context_private)}\t:\t{form.project_context_private.data} \n
        {extract_label(form.project_summary.label)}\t:\t{form.project_summary.data} \n
        {extract_label(form.bioF_needs.label)}\t:\t{form.bioF_needs.data} \n
        {extract_label(form.data_available.label)}\t:\t{form.data_available.data} \n

                ***************************************

        {extract_label(form.access_data.label)}\t:\t{form.access_data.data} \n
        {extract_label(form.data_owner.label)}\t:\t{form.data_owner.data} \n
        {extract_label(form.regulatory_requirements.label)}\t:\t{form.regulatory_requirements.data} \n
        {extract_label(form.if_regulatory_requirements.label)}\t:\t{form.if_regulatory_requirements.data} \n

                ***************************************

        {extract_label(form.data_type.label)}\t:\t{form.data_type.data} \n
        {extract_label(form.data_size.label)}\t:\t{form.data_size.data} \n
        {extract_label(form.add_info.label)}\t:\t{form.add_info.data} \n
    '''
    return body

def object_grant(form):
    grant = Grant(
        username = form.username.data,
        email = form.email.data,
        author = current_user,
        project_token = secrets.token_bytes(32).hex(),
        project_title = form.project_title.data,
        application = form.application.data,
        organism = form.organism.data,
        principal_investigator = form.principal_investigator.data,
        promotor = form.promotor.data,
        urgency_of_request = form.urgency_of_request.data,
        if_urgency = form.if_urgency.data,
        project_context = form.project_context.data,
        project_context_private = form.project_context_private.data,
        project_summary = form.project_summary.data,
        bioF_needs = form.bioF_needs.data,
        data_available = form.data_available.data,
        access_data = form.access_data.data,
        data_owner = form.data_owner.data,
        regulatory_requirements = form.regulatory_requirements.data,
        if_regulatory_requirements = form.if_regulatory_requirements.data,
        data_type = form.data_type.data,
        data_size = form.data_size.data,
        add_info = form.add_info.data,
        funding_type = form.funding_type.data,
        total_amount = form.total_amount.data,
        deadline = form.deadline.data
    )

    return grant
