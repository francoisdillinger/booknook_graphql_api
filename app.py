from app.main import create_app
from flask_graphql import GraphQLView
from graphene import  Schema
from app.graphQL.queries import Query

app = create_app()
schema = Schema(query=Query)

app.add_url_rule(
    "/graphql",
    view_func=GraphQLView.as_view(
        "graphql",
        schema=schema,
        graphiql=True  # Enable GraphiQL when app.debug is True. GraphiQL is an interactive in-browser GraphQL IDE.
    )
)

@app.route("/")
def hello_world():
    return "Hello, World!"

if __name__ == "__main__":
    app.run(debug=True)