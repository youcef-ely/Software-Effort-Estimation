#Defining a dictionary for categorial data

from sympy import re


def values_meaning(col_name):
    dd = None
    if col_name == 'Organization type':
        dd = {1:'Public Software company', 2:'University', 3:'Federal Ministry', 4:'Federal directorates', 5:'Private Software company', 6:'Corporate IT department', 7:'Freelancer', 8:'Telecommunication company'}
    if col_name == 'Role in organization':
        dd = {1:'Developer', 2:'Project manager', 3:'Company manager', 4:'Technical consultant', 6:'Technical manager', 7:'Planning coordinator', 8:'System administrator'}
    if col_name == 'Customer organization type':
        dd = {1:'University department', 2:'Department in a Private company', 3:'Bank', 4:'Federal Ministry', 5:'Department in a federal ministry', 6:'Factory', 7:'Hospital department', 8:'TV Channel', 9:'Non-profit organization', 10:'Private company', 11:'Hospital', 12:'Public company', 13:'In-house development', 14:'Federal directorates', 15:'Private school', 16:'Department in a bank'}
    
    if col_name == 'Size of organization':
        dd = {1:'1-5', 2:'6-10', 3:'11-20', 4:'21-30', 5:'31-40', 6:'41-50', 7:'51-100', 8:'101-150', 9:'151-200', 10:'201-250', 11:'251-300', 12:'301-350', 13:'351-400', 14:'401-450', 15:'451-500', 16:'>500'}
    if col_name == 'Size of IT department':
        dd = {1:'1-5', 2:'6-10', 3:'11-15', 4:'16-20', 5:'21-25', 6: '26-30', 7:'31-35', 8:'36-40', 9:'41-45', 10:'46-50', 11:'>50', 12:'N/A'}
    if col_name == 'Application domain':
        dd = {1:'Banking systems', 2:'ERP', 3:'Mobile applications', 5:'Financial and managerial', 6: 'Web applications', 7:'Bespoke applications'}
    if col_name == 'Development type':
        dd = {1:'New software development', 2:'Upgrading existing software', 3:'Modifying existing software', 4:'Customization of imported software'}
    
    
    if col_name == 'Government policy impact':
        dd = {1:'Very positive impact', 2:'Positive impact', 3:'No impact', 4:'Negative impact', 5:'Very negative impact'}
    if col_name == 'Developer hiring policy':
        dd = {1:'There exists hiring standards and applicant evaluations and are applied', 2:'No hiring standards but applicant evaluation is applied', 3:'There exists hiring standards and applicant evaluations but are not implemented – hiring acquaintances', 4:'No specific policy followed'}
    if col_name == 'Organization management structure clarity':
        dd = {1:'Organization management structure is clear and all procedures are clear', 2:'Organization management structure isn’t clear', 3:'No organization management structure exists'}
    if col_name == 'Incentive policy implementation level':
        dd = {1:'Incentives based on clear metrics', 2:'Incentives based on personal considerations of CEO/project manager', 3:'No incentives'}
    if col_name == 'Developer training':
        dd = {1:'Organization provides periodic training which was utilized', 2:'Developers were trained specifically for this project', 3:'No training provided'}
    if col_name in ['Fixed minimum working hours', 'Time sheet recording', 'Team work commitment', 'Top management opinion of previous system','Direct automation of the manual system', 'Transfer of key user', 'DBMS expert availability', 'Open source software', 'Risk plan', 'Risk management tool usage', 'Reengineering']:
        dd = {1:'Yes', 0:'No'}  
    if col_name == 'Consequence for lack of work':
        dd = {1:'Dismissal from work', 2:'Salary deduction', 3:'Warning', 4:'No consequences'}
    if col_name == 'Absence policy implementation':
        dd = {1:'Rules and its applied', 2:'Rules and it’s not applied', 3:'No rules'} 
   
    
    if col_name == 'User manual clarity':
        dd = {1:'Very clear', 2:'Clear', 3:'Normal', 4:'Unclear', 5:'Very unclear'}
    if col_name in ['Modifications during requirements collection', 'Modifications during analysis', 'Modifications during design', 'Modifications during programming', 'Modifications during testing', 'Modifications during deployment']:
        dd = {0:'No changes', 1:'Minor', 2:'Partial', 3:'Major'}
    if col_name == 'User computer experience':
        dd = {1:'Previous computer system exists in the customer organization', 2:'Familiar with the basics', 3:'No computer experience'}
    if col_name in ['Manual system experience', 'User cooperation in requirement solicitation', 'Users desire for change/project adaption', 'User not afraid of the impact of product', 'Cohesion between developers and users']:
        dd = {1:'Very strong', 2:'Strong', 3:'Normal', 4:'Weak', 5:'Very weak'}
    
    
    if col_name == 'Project manager experience':
        dd = {1:'Previous experience in similar software systems', 2:'Previous experience in non- similar software systems', 3:'No previous experience'}
    if col_name == 'Consultant availability':
        dd = {1:'A consultant advised on the technical and project management issues', 2:'A consultant advised on the technical issues only', 3:'No consultancy'}
    if col_name in ['Software tool experience', 'Programmers experience in programming language']:
        dd = {1:'More than 4 years', 2:'2 years - 3 years', 3:'1 year – 2 years', 4:'6 months – 1 year', 5:'First time in this project'}
    if col_name == 'Team selection':
        dd = {1: 'Based on experience in application type', 2:'Based on job specialization (analysts, designers, ..., etc.)', 3:'Based on existing developers'}
    if col_name == 'Income satisfaction':
        dd = {1:'Very satisfied', 2:'Satisfied', 3:'Normal', 4:'Unsatisfied', 5:'Very unsatisfied'}
    
    
    if col_name == 'Schedule quality':
        dd = {1:'Devised a schedule and followed it with periodic evaluation', 2:'Devised a schedule with no periodic evaluation', 3:'Devised a schedule and did not follow it', 4:'No schedule'}
    if col_name == 'Programming language used':
        dd = {1:'PHP', 2:'Android', 3:'ASP.net', 4:'C#', 5:'Java, Android', 6:'Java', 7:'Oracle Developer', 8:'Visual Basic 6', 9:'Python/Java', 10:'Python', 11:'Visual Basic .Net', 12:'C++', 13:'Python/HTML/PHP', 16:'Visual Basic/C#', 17:'PHP/Oracle', 18:'Javascript/PHP', 19:'ASP.NET/Javascript/C#', 23:'CH', 24:'Java, C#, PHP', 25:'Java/Android/C#'}
    if col_name == 'DBMS used':
        dd = {1:'MySQL', 2:'Oracle', 3:'Microsoft SQL Server', 5:'PostgreSQL'}
    if col_name == 'Methodology':
        dd = {1:'Waterfall', 2:'Agile', 3:'Hybrid methodologies', 4:'No methodology', 6:'Prototyping', 7:'Other'}
    if col_name == 'Level of technical instability (Main)':
        dd = {1:'No technology change', 2:'one time during project development', 3:'2 – 3 times', 4:'Frequent changes'}
    if col_name == 'Level of outsourcing': 
        dd = {1:'Outsourcing to an entity with better experience and capabilities than the development team', 2:'Outsourcing to an entity with the same experience and capabilities as the development team', 3:'No outsourcing'}
    if col_name == 'Outsourcing impact': 
        dd = {1: 'Schedule underrun', 2:'No effect', 3:'Schedule overrun', 5:'No answer'}
    if col_name == 'Degree of software reuse':
        dd = {1:'Reuse/purchase a complete software system', 2:'Reuse/purchase modules from previous software system', 3:'Reuse the design of a previous software system', 4:'Reuse the technical specifications from previous software system', 5:'No reuse'}
    if col_name == 'Use of standards': 
        dd = {1: 'Use of standards for all the software development lifecycle', 2: 'Use of standards for specific phases in software development lifecycle', 3: 'Not using any standards'}
    
    
    
    if col_name == 'Requirement accuracy level':
        dd = {1:'Accurate requirements specifications used to develop the software system', 2:'Inaccurate requirements specifications and required the re-analysis of the software requirements', 3:'Inaccurate requirements specifications and required the re-design of the software system', 4:'Inaccurate requirements specifications and required re-programming the software system'}
    if col_name == 'Technical documentation':
        dd = {1:'No documentation', 2:'Large parts of the development lifecycle not covered', 3:'Minimal parts of the development lifecycle not covered', 4:'All phases were documented'} 
    if col_name == 'Comments within the code':
        dd = {1:'No comments', 2:'Comments for programmer’s convenience', 3:'Comments in some modules for other programmers understanding', 4:'Detailed comments within the code'}
    if col_name == 'User manual':
        dd = {1:'No user manual', 2:'User manual does not cover all the software system', 3:'Unclear user manual, written in technical terminology', 4:'Clear user manual that covers all the software system'}
    if col_name == 'Required reusability':
        dd = {1:'No reusing required', 2:'Reusing of some modules', 3:'Reusing of the complete software system to develop another software system', 4:'Customizations of the software system to be sold to other customers'}
    if col_name == 'Product complexity':
        dd = {1:'User dis-satisfaction and inconvenience', 2:'Minor monetary loss, can be mitigated', 3:'Medium monetary loss, can be mitigated', 4:'Major monetary loss', 5:'Life threatening'}
    if col_name == 'Reliability requirements':
        dd = {1:'User dis-satisfaction and inconvenience', 2:'Minor monetary loss, can be mitigated', 3:'Medium monetary loss, can be mitigated', 4:'Major monetary loss', 5:'Life threatening'}
    if col_name == 'Specified H/W':
        dd = {1:'Not required', 2:'Required specialized H/W that was available on time and we have prior experience with the H/W', 3:'Required specialized H/W that was available on time but we do not have prior experience with the H/W', 4:'Required specialized H/W that was not available on time'}
     
    return dd



def categorical_cols_names():
    names = ['Organization type', 'Role in organization', 'Size of organization', 'Customer organization type',  'Application domain', 'Development type', 'Size of IT department',
    'Government policy impact', 'Organization size', 'Developer hiring policy', 'Organization management structure clarity', 'Developer training', 'Fixed minimum working hours', 'Time sheet recording', 'Team work commitment', 'Top management opinion of previous system','Direct automation of the manual system', 'Transfer of key user', 'DBMS expert availability', 'Open source software', 'Risk plan', 'Risk management tool usage', 'Reengineering', 'Consequence for lack of work', 'Absence policy implementation',
    'User manual clarity', 'Manual system experience', 'User cooperation in requirement solicitation', 'Users desire for change/project adaption', 'User not afraid of the impact of product', 'Cohesion between developers and users',
    'Project manager experience', 'Consultant availability', 'Software tool experience', 'Programmers experience in programming language', 'Team selection', 'Income satisfaction',
    'Schedule quality', 'Programming language used', 'DBMS used', 'Methodology', 'Level of outsourcing', 'Outsourcing impact', 'Degree of software reuse', 'Use of standards', 
    'Requirement accuracy level', 'Technical documentation', 'Comments within the code', 'User manual', 'Required reusability', 'Product complexity', 'Reliability requirements', 'Specified H/W']
    names.sort()
    return names


#Defining a dictionary for each category and its columns
def categories(category):
    categories = {
    'General Information': ['Year of project', 'Organization type', 'Role in organization', 'Size of organization', 
                            'Size of IT department', 'Customer organization type', 'Estimated  duration', 'Actual duration', 
                            '% project gain (loss)', 'Development type', 'Application domain'
                           ],
    'Size':                ['Object points', 'Other sizing method', 'Estimated size'
                           ],
    'Effort':              ['Estimated effort', 'Actual effort'
                           ],
    'Environment':         ['Contract maturity', 'Government policy impact', 'Economic instability impact',
                            'Organization management structure clarity', 'Developer hiring policy',
                            'Developer incentives policy', 'Developer training',
                            'Development team management'
                           ],
    'Users':               ['Top management support',
                            'Top management opinion of previous system', 'Clarity of manual system',
                            'User resistance', 'User computer experience', 'Users stability',
                            'Requirment stability', 'Requirements flexibility'
                           ],
    'Developers':          ['Project manager experience', 'Consultant availability', 'DBMS expert availability', 'Precedentedness',
                            'Software tool experience', 'Programmers experience in programming language', 'Programmers capability ', 'Analysts capability', 
                            'Team selection', 'Team size', 'Dedicated team members', 'Daily working hours', 'Team contracts', 'Team continuity', 
                            'Team cohesion', 'Income satisfaction'
                           ],
    'Project':             ['Schedule quality', 'Development environment adequacy', 'Tool availability', 'Methodology',
                            'Multiple programing languages', 'Programming language used',
                            'DBMS used', 'Technical stability', 'Open source software',
                            'Level of outsourcing', 'Outsourcing impact',
                            'Degree of software reuse', 'Degree of risk management',
                            'Use of standards', 'Degree of standards usage',
                            'Process reengineering'
                           ], 
    'Product':             ['Requirement accuracy level',
                            'Technical documentation', 'Comments within the code', 'User manual',
                            'Required reusability', 'Performance requirements',
                            'Product complexity', 'Security requirements',
                            'Reliability requirements', 'Specified H/W'
                            ], 
    }
    
    return categories[category]

def ordinal_categories():
    return ['Size of organization', 'Size of IT department', 'Government policy impact', 'User manual', 'Users stability',
            'Programmers experience in programming language', 'Software tool experience', 'Income satisfaction', 'Product complexity',
            'Reliability requirements']