"""
chris.wiggins@gmail.com 2024-04-08
"""
import arxiv

# Construct the default API client
client = arxiv.Client()

# Search for articles with titles containing "all you need"
search = arxiv.Search(
  query = 'ti:"all you need"',
  max_results = 10000,  # Adjust max_results as needed
  sort_by = arxiv.SortCriterion.SubmittedDate,
  sort_order = arxiv.SortOrder.Descending
)

# Execute the search and process results
results = client.results(search)

print("Titles containing 'all you need':")
for result in results:
    print(f"- {result.title} (Published on: {result.published})")
