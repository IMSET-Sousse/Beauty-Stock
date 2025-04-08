"use client"

import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer } from "recharts"
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card"
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs"
import { ChartContainer } from "@/components/ui/chart"

const stockData = [
  { category: "Skincare", inStock: 245, lowStock: 18, outOfStock: 5 },
  { category: "Makeup", inStock: 187, lowStock: 24, outOfStock: 8 },
  { category: "Hair Care", inStock: 132, lowStock: 15, outOfStock: 3 },
  { category: "Fragrance", inStock: 98, lowStock: 12, outOfStock: 2 },
  { category: "Body Care", inStock: 156, lowStock: 9, outOfStock: 4 },
  { category: "Nail Care", inStock: 76, lowStock: 6, outOfStock: 1 },
]

const categoryData = [
  { name: "Skincare", value: 268 },
  { name: "Makeup", value: 219 },
  { name: "Hair Care", value: 150 },
  { name: "Fragrance", value: 112 },
  { name: "Body Care", value: 169 },
  { name: "Nail Care", value: 83 },
]

export function StockLevels() {
  return (
    <Tabs defaultValue="overview" className="space-y-4">
      <TabsList>
        <TabsTrigger value="overview">Overview</TabsTrigger>
        <TabsTrigger value="categories">Categories</TabsTrigger>
      </TabsList>
      <TabsContent value="overview" className="space-y-4">
        <div className="h-[300px]">
          <ChartContainer
            config={{
              inStock: {
                label: "In Stock",
                color: "hsl(var(--chart-1))",
              },
              lowStock: {
                label: "Low Stock",
                color: "hsl(var(--warning))",
              },
              outOfStock: {
                label: "Out of Stock",
                color: "hsl(var(--destructive))",
              },
            }}
          >
            <ResponsiveContainer width="100%" height="100%">
              <BarChart
                data={stockData}
                margin={{
                  top: 20,
                  right: 30,
                  left: 20,
                  bottom: 5,
                }}
              >
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis dataKey="category" />
                <YAxis />
                <Tooltip />
                <Bar dataKey="inStock" stackId="a" fill="var(--color-inStock)" />
                <Bar dataKey="lowStock" stackId="a" fill="var(--color-lowStock)" />
                <Bar dataKey="outOfStock" stackId="a" fill="var(--color-outOfStock)" />
              </BarChart>
            </ResponsiveContainer>
          </ChartContainer>
        </div>
        <div className="grid gap-4 md:grid-cols-2 lg:grid-cols-3">
          <Card>
            <CardHeader className="pb-2">
              <CardTitle>Total Products</CardTitle>
              <CardDescription>All products in inventory</CardDescription>
            </CardHeader>
            <CardContent>
              <div className="text-2xl font-bold">1,248</div>
              <p className="text-xs text-muted-foreground">Across 6 categories</p>
            </CardContent>
          </Card>
          <Card>
            <CardHeader className="pb-2">
              <CardTitle>Low Stock</CardTitle>
              <CardDescription>Products below threshold</CardDescription>
            </CardHeader>
            <CardContent>
              <div className="text-2xl font-bold">84</div>
              <p className="text-xs text-muted-foreground">Need reordering soon</p>
            </CardContent>
          </Card>
          <Card>
            <CardHeader className="pb-2">
              <CardTitle>Out of Stock</CardTitle>
              <CardDescription>Products with zero inventory</CardDescription>
            </CardHeader>
            <CardContent>
              <div className="text-2xl font-bold">23</div>
              <p className="text-xs text-muted-foreground">Require immediate attention</p>
            </CardContent>
          </Card>
        </div>
      </TabsContent>
      <TabsContent value="categories" className="space-y-4">
        <div className="h-[300px]">
          <ChartContainer
            config={{
              value: {
                label: "Products",
                color: "hsl(var(--chart-1))",
              },
            }}
          >
            <ResponsiveContainer width="100%" height="100%">
              <BarChart
                data={categoryData}
                margin={{
                  top: 20,
                  right: 30,
                  left: 20,
                  bottom: 5,
                }}
              >
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis dataKey="name" />
                <YAxis />
                <Tooltip />
                <Bar dataKey="value" fill="var(--color-value)" />
              </BarChart>
            </ResponsiveContainer>
          </ChartContainer>
        </div>
        <div className="grid gap-4 md:grid-cols-2">
          <Card>
            <CardHeader>
              <CardTitle>Top Categories</CardTitle>
              <CardDescription>By number of products</CardDescription>
            </CardHeader>
            <CardContent>
              <div className="space-y-4">
                <div className="flex items-center">
                  <div className="w-[120px] font-medium">Skincare</div>
                  <div className="flex-1">
                    <div className="h-2 w-full rounded-full bg-muted">
                      <div className="h-2 rounded-full bg-primary" style={{ width: "80%" }}></div>
                    </div>
                  </div>
                  <div className="ml-4 w-[60px] text-right font-medium">268</div>
                </div>
                <div className="flex items-center">
                  <div className="w-[120px] font-medium">Makeup</div>
                  <div className="flex-1">
                    <div className="h-2 w-full rounded-full bg-muted">
                      <div className="h-2 rounded-full bg-primary" style={{ width: "65%" }}></div>
                    </div>
                  </div>
                  <div className="ml-4 w-[60px] text-right font-medium">219</div>
                </div>
                <div className="flex items-center">
                  <div className="w-[120px] font-medium">Body Care</div>
                  <div className="flex-1">
                    <div className="h-2 w-full rounded-full bg-muted">
                      <div className="h-2 rounded-full bg-primary" style={{ width: "50%" }}></div>
                    </div>
                  </div>
                  <div className="ml-4 w-[60px] text-right font-medium">169</div>
                </div>
                <div className="flex items-center">
                  <div className="w-[120px] font-medium">Hair Care</div>
                  <div className="flex-1">
                    <div className="h-2 w-full rounded-full bg-muted">
                      <div className="h-2 rounded-full bg-primary" style={{ width: "45%" }}></div>
                    </div>
                  </div>
                  <div className="ml-4 w-[60px] text-right font-medium">150</div>
                </div>
              </div>
            </CardContent>
          </Card>
          <Card>
            <CardHeader>
              <CardTitle>Category Growth</CardTitle>
              <CardDescription>Month over month</CardDescription>
            </CardHeader>
            <CardContent>
              <div className="space-y-4">
                <div className="flex items-center">
                  <div className="w-[120px] font-medium">Fragrance</div>
                  <div className="flex-1">
                    <div className="h-2 w-full rounded-full bg-muted">
                      <div className="h-2 rounded-full bg-green-500" style={{ width: "25%" }}></div>
                    </div>
                  </div>
                  <div className="ml-4 w-[60px] text-right font-medium text-green-500">+25%</div>
                </div>
                <div className="flex items-center">
                  <div className="w-[120px] font-medium">Skincare</div>
                  <div className="flex-1">
                    <div className="h-2 w-full rounded-full bg-muted">
                      <div className="h-2 rounded-full bg-green-500" style={{ width: "18%" }}></div>
                    </div>
                  </div>
                  <div className="ml-4 w-[60px] text-right font-medium text-green-500">+18%</div>
                </div>
                <div className="flex items-center">
                  <div className="w-[120px] font-medium">Makeup</div>
                  <div className="flex-1">
                    <div className="h-2 w-full rounded-full bg-muted">
                      <div className="h-2 rounded-full bg-green-500" style={{ width: "12%" }}></div>
                    </div>
                  </div>
                  <div className="ml-4 w-[60px] text-right font-medium text-green-500">+12%</div>
                </div>
                <div className="flex items-center">
                  <div className="w-[120px] font-medium">Nail Care</div>
                  <div className="flex-1">
                    <div className="h-2 w-full rounded-full bg-muted">
                      <div className="h-2 rounded-full bg-red-500" style={{ width: "5%" }}></div>
                    </div>
                  </div>
                  <div className="ml-4 w-[60px] text-right font-medium text-red-500">-5%</div>
                </div>
              </div>
            </CardContent>
          </Card>
        </div>
      </TabsContent>
    </Tabs>
  )
}
