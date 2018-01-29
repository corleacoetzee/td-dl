from setuptools import setup

setup(
    name='data-lineage',
    version='0.0.1',
    description='Api for data lineage on neo4j',
    author='bluetab',
    author_email='bluetab@bluetab.net',
    license = 'Apache2 License',
    keywords = ['data-lineage', 'api', 'neo4j'],
    packages=['api', 'api.v1', 'api.common', 'api.settings', 'api.models'],
    include_package_data=True,
    install_requires=[
        'astroid==1.6.0',
        'click==6.7',
        'coverage==4.4.2',
        'gunicorn==19.7.1',
        'Fabric3==1.13.1.post1',
        'flasgger==0.6.3',
        'Flask==0.12.2',
        'Flask-Cors==3.0.2',
        'Flask-HTTPAuth==3.2.3',
        'Flask-SQLAlchemy==2.3.2',
        'isort==4.2.15',
        'itsdangerous==0.24',
        'Jinja2==2.9.6',
        'jsonschema==2.6.0',
        'lazy-object-proxy==1.3.1',
        'MarkupSafe==1.0',
        'mccabe==0.6.1',
        'mistune==0.7.4',
        'neo4j-driver==1.3.0',
        'nose2==0.7.3',
        'passlib==1.7.1',
        'PyYAML==3.12',
        'six==1.11.0',
        'tornado==4.5.2',
        'Werkzeug==0.12.2',
        'wrapt==1.10.11'
    ],
)
