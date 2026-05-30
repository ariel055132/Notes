---
type: concept
aliases: ["object store", "object storage service", "media storage", "file object storage"]
tags: [system-design, storage, cdn]
created: 2026-05-26
updated: 2026-05-26
source_count: 2
---

# Object Storage

## Definition

Object storage is a durable storage layer for files or blobs where objects are addressed by keys, commonly used as the origin for CDN-served images, video segments, PDFs, SDK packages, and other static or media assets. [[2026-05-15--cdn-content-delivery-network|CDN (Content Delivery Network)]] In database selection, large media files and documents should usually go to blob or object storage rather than being stored directly inside an application database. [[2026-04-15--database|Database]]

## Scope

This concept covers storing uploaded or generated assets durably, recording object keys in metadata databases, and letting CDN fetch objects on demand from the storage origin. [[2026-05-15--cdn-content-delivery-network|CDN (Content Delivery Network)]] It does not make edge cache the source of truth: CDN entries can be evicted and can differ by region, while object storage or origin remains the authoritative copy for files. [[2026-05-15--cdn-content-delivery-network|CDN (Content Delivery Network)]] The database overview uses file storage as an explicit non-database case: images, videos, and large documents belong in blob storage, with metadata kept separately. [[2026-04-15--database|Database]]

## Contrasts

- **CDN and Edge Caching**: Object storage provides durable origin storage, while CDN provides nearby cached delivery and origin offload. [[2026-05-15--cdn-content-delivery-network|CDN (Content Delivery Network)]]
- **Metadata Database**: Object storage holds bytes under object keys, while a metadata database records ownership, permissions, transformations, and references to those objects. [[2026-05-15--cdn-content-delivery-network|CDN (Content Delivery Network)]]
- **Distributed Cache**: Distributed cache accelerates application read paths for rebuildable data, while object storage is a durable file source often fronted by CDN. [[2026-05-15--distributed-cache|Distributed Cache]] [[2026-05-15--cdn-content-delivery-network|CDN (Content Delivery Network)]]
- **Database**: Databases should usually store metadata and references for large files, while object storage holds the bytes. [[2026-04-15--database|Database]]

## Evidence

- [[2026-05-15--cdn-content-delivery-network|CDN (Content Delivery Network)]] — The source describes upload to object storage, metadata database recording the object key, and CDN fetching objects on demand.
- [[2026-04-15--database|Database]] — The source says simple file storage for images, videos, and large documents should use blob storage rather than putting files directly in a database.

## Related

- [[database|Database]]
- [[database-selection|Database Selection]]
- [[cdn-and-edge-caching|CDN and Edge Caching]]
- [[signed-cdn-access|Signed CDN Access]]
- [[cdn-cache-key-design|CDN Cache-Key Design]]
- [[cache-invalidation|Cache Invalidation]]

## Open Questions

- Which future source should cover object storage consistency, lifecycle policy, multipart upload, and generated derivative assets?
