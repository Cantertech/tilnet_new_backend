# TILNET Admin Dashboard Guide

## Overview
The TILNET Admin Dashboard is a comprehensive analytics and management tool that provides administrators with detailed insights into user activity, revenue, customer behavior, and system performance.

## Features

### 📊 Dashboard Tabs

#### 1. Overview Tab
- **Total Users**: Complete user count and active users (30 days)
- **Total Estimates**: Manual estimates, project estimates, and 3D estimates
- **Supplier Statistics**: Total, verified, and active suppliers
- **Revenue Metrics**: Total revenue, conversion rates, and breakdowns
- **Quick Insights**: Key performance indicators and engagement metrics
- **Top Performing Suppliers**: Ranked list with ratings and order counts

#### 2. Users Tab
- **User Analytics**: Total users, paying users, active users
- **Conversion Rate**: Percentage of users who have made payments
- **Registration Trends**: Daily user registration charts (last 30 days)
- **User Engagement**: Average estimates per user

#### 3. Suppliers Tab
- **Supplier Analytics**: Total, verified, and active supplier counts
- **Product Statistics**: Total products and in-stock items
- **Order Tracking**: Total supplier orders and delivery status
- **Verification Status**: Percentage of verified suppliers

#### 4. Revenue Tab
- **Revenue Breakdown**: Total, subscription, and supplier revenue
- **Payment Analytics**: Success rates and payment status tracking
- **Revenue Trends**: Monthly revenue charts and estimates per day
- **Conversion Metrics**: User conversion to paying customers

#### 5. Customers Tab (NEW)
- **Customer Analytics**: Total customers and engagement rates
- **Top Customers**: Ranked by number of projects created
- **Geographic Distribution**: Top locations by customer count
- **Customer Engagement**: Percentage of customers with active projects

#### 6. Analytics Tab (NEW)
- **Comprehensive Revenue Analytics**: Detailed payment statistics and trends
- **Project Type Analytics**: Breakdown by project categories (tiling, masonry, etc.)
- **Top Users by Projects**: Most active users ranked by project count
- **Subscription Analytics**: Active subscriptions and plan distribution

### 📈 Export Functionality
- **CSV Export**: Download detailed reports for:
  - Customers (with project counts and engagement data)
  - Revenue (payment transactions and subscription data)
  - Projects (all project details and customer information)
  - Users (user profiles, activity, and subscription status)

## API Endpoints

### Authentication
- `POST /api/admin/login/` - Superuser login with JWT tokens

### Analytics
- `GET /api/admin/stats/` - Basic dashboard statistics
- `GET /api/admin/analytics/` - Comprehensive analytics data
- `GET /api/admin/reports/?type={type}` - Detailed reports for export

### User Management
- `GET /api/admin/users/` - List all users
- `POST /api/admin/users/` - Create new user
- `GET /api/admin/users/{id}/` - Get user details
- `PUT /api/admin/users/{id}/` - Update user
- `DELETE /api/admin/users/{id}/` - Delete user

## Key Metrics Tracked

### User Metrics
- Total registered users
- Active users (logged in within 30 days)
- Paying users (with active subscriptions)
- User conversion rate
- Average projects per user

### Revenue Metrics
- Total revenue from all sources
- Subscription revenue
- Supplier marketplace revenue
- Payment success rates
- Average payment amounts
- Monthly revenue trends

### Customer Metrics
- Total customers
- Customers with active projects
- Customer engagement rate
- Geographic distribution
- Top customers by project count

### Project Metrics
- Total estimates created
- Project types distribution
- Estimates per day trends
- Project completion rates
- Customer project counts

### Supplier Metrics
- Total suppliers registered
- Verified supplier percentage
- Active suppliers
- Total products listed
- Supplier orders and ratings

## Security Features

- **Superuser Authentication**: Only superusers can access the admin dashboard
- **JWT Token Security**: Secure token-based authentication
- **Permission-based Access**: Role-based access control
- **Data Validation**: Server-side validation for all operations

## Usage Instructions

### 1. Accessing the Dashboard
1. Navigate to the admin dashboard URL
2. Login with superuser credentials
3. Dashboard will automatically load with current data

### 2. Viewing Analytics
1. Use the tab navigation to switch between different views
2. All data is automatically refreshed on login
3. Charts and graphs provide visual representations of trends

### 3. Exporting Data
1. Click on any export button in the header
2. CSV file will be automatically downloaded
3. Files are named with the report type and current date

### 4. User Management
1. Navigate to the Users tab
2. View user statistics and registration trends
3. Use export functionality to get detailed user reports

## Technical Implementation

### Backend
- Django REST Framework
- Custom admin API endpoints
- Comprehensive data aggregation
- Secure authentication system

### Frontend
- React with TypeScript
- Responsive design
- Real-time data visualization
- CSV export functionality

### Database
- Optimized queries with aggregations
- Efficient data relationships
- Indexed fields for performance

## Performance Considerations

- **Data Caching**: Analytics data is cached for better performance
- **Optimized Queries**: Uses select_related and prefetch_related for efficiency
- **Pagination**: Large datasets are paginated for better loading times
- **Lazy Loading**: Components load data only when needed

## Future Enhancements

- Real-time notifications for important events
- Advanced filtering and search capabilities
- Interactive charts and graphs
- Automated report scheduling
- Email report delivery
- Advanced user segmentation
- A/B testing analytics
- Mobile-responsive improvements

## Troubleshooting

### Common Issues
1. **Login Failed**: Ensure superuser credentials are correct
2. **Data Not Loading**: Check network connection and API endpoints
3. **Export Not Working**: Verify browser allows downloads
4. **Charts Not Displaying**: Check if data exists for the selected time period

### Support
For technical support or feature requests, contact the development team.
